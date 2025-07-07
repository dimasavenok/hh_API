from typing import Self, Optional

import psycopg2
from psycopg2.extensions import connection


class DBManager:
    def __init__(self: Self, connect_params: dict[str, str]) -> None:
        self.connect_params: dict[str, str] = connect_params
        self.conn: connection = self.connect()
        # self.__reset_database()
        # self.__create_tables()


    def connect(self) -> connection:
        try:
            return psycopg2.connect(
                dbname=self.connect_params.get("dbname"),
                user=self.connect_params.get("user"),
                password=self.connect_params.get("password"),
                host=self.connect_params.get("host"),
                port=self.connect_params.get("port")
            )
            # return psycopg2.connect(
            #     dbname="hh_db",
            #     user="postgres",
            #     password="hh_password",
            #     host="localhost",
            #     port="5432"
            # )
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
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS companies 
                (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE
                );
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS vacancies
                (
                id SERIAL PRIMARY KEY,
                company_id INTEGER REFERENCES companies(id) ON DELETE CASCADE,
                title VARCHAR(255) NOT NULL,
                salary FLOAT DEFAULT NULL,
                url TEXT NOT NULL 
                description TEXT DEFAULT NULL
                );
                """)
        self.conn.commit()

    def insert_company(self, name: str):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO companies (name)
            VALUES (%s);
            """, (name,))
        self.conn.commit()

    def insert_vacancy(
            self,
            title: str,
            salary: float,
            url: str,
            description: str,
            company_name: str
    ):
        company_id = self.get_company_id_by_name(company_name)
        if company_id is None:
            self.insert_company(name=company_name)
            company_id = self.get_company_id_by_name(company_name)
        if company_id is None:
            return
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO vacancies (company_id, title, salary, url, description)
            VALUES (%s, %s, %s, %s, %s);
            """, (company_id, title, salary, url, description))
        self.conn.commit()


    def get_company_id_by_name(self, name) -> Optional[int]:
        with self.conn.cursor() as cur:
            cur.execute("""
                        SELECT id FROM companies
                        WHERE name = "%s";
                        """, (name,))
        self.conn.commit()