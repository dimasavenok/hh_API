from typing import Self, Optional, Any
import psycopg2
from psycopg2.extensions import connection


class DBManager:
    def __init__(self: Self, connect_params: dict[str, str]) -> None:
        self.connect_params: dict[str, str] = connect_params
        self.conn: connection = self.connect()
        self.__reset_database()
        self.__create_tables()

    def connect(self) -> connection:
        try:
            return psycopg2.connect(
                dbname=self.connect_params.get("dbname"),
                user=self.connect_params.get("user"),
                password=self.connect_params.get("password"),
                host=self.connect_params.get("host"),
                port=self.connect_params.get("port")
            )
        except psycopg2.Error:
            raise
        except Exception:
            raise

    def __reset_database(self):
        with self.conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS vacancies CASCADE;")
            cur.execute("DROP TABLE IF EXISTS companies CASCADE;")
        self.conn.commit()

    def __create_tables(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS companies (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL UNIQUE
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    id SERIAL PRIMARY KEY,
                    company_id INTEGER REFERENCES companies(id) ON DELETE SET NULL,
                    title VARCHAR(255) NOT NULL,
                    salary FLOAT DEFAULT NULL,
                    url TEXT NOT NULL,
                    description TEXT DEFAULT NULL
                );
            """)
        self.conn.commit()

    def insert_company(self, name: str):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO companies (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING;
            """, (name,))
        self.conn.commit()

    def insert_vacancy(
        self,
        title: str,
        salary: float,
        url: str,
        description: str,
        company_name: Optional[str] = None
    ):
        company_id = None
        if company_name:
            company_id = self.get_company_id_by_name(company_name)
            if company_id is None:
                self.insert_company(name=company_name)
                company_id = self.get_company_id_by_name(company_name)

        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO vacancies (company_id, title, salary, url, description)
                VALUES (%s, %s, %s, %s, %s);
            """, (company_id, title, salary, url, description))
        self.conn.commit()

    def get_company_id_by_name(self, name: str) -> Optional[int]:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id FROM companies
                WHERE name = %s;
            """, (name,))
            result = cur.fetchone()
            return result[0] if result else None

    def get_companies_and_vacancies_count(self) -> Optional[list[tuple[str, int]]]:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, COUNT(v.id) AS vacancy_count 
                FROM companies c
                LEFT JOIN vacancies v ON c.id = v.company_id
                GROUP BY c.id
                ORDER BY vacancy_count DESC;
            """ )
            return cur.fetchall()

    def get_all_vacancies(self) -> Optional[list[tuple[Any]]]:
        with self.conn.cursor() as cur:
            cur.execute("""
                       SELECT c.name, v.title, v.salary, v.url
                       FROM vacancies v
                       LEFT JOIN companies c ON c.id = v.company_id;
                   """)
            return cur.fetchall()

    def get_avg_salary(self) -> Optional[float]:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT AVG(salary)
                FROM vacancies
                WHERE salary IS NOT NULL;
            """)
            result = cur.fetchone()
            return result[0] if result else None

    def get_vacancies_with_higher_salary(self) -> list[tuple[str, str, float]]:
        avg_salary = self.get_avg_salary()
        if avg_salary is None: return []
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, v.title, v.salary
                FROM vacancies v
                LEFT JOIN companies c ON c.id = v.company_id
                WHERE v.salary > %s;
            """, (avg_salary,))
            return cur.fetchall()

    def get_vacancies_with_keyword(self, keyword: str) -> list[tuple]:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT v.title, v.salary
                FROM vacancies v
                WHERE v.title LIKE %s;
            """, (f"%{keyword}%",))
            return cur.fetchall()


