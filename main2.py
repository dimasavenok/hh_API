import json

from src.storage.DBManager import DBManager

connect_params = {
    "dbname": "hh_db",
    "user": "postgres",
    "password": "dima510141",
    "host": "localhost",
    "port": "5432"
}

db: DBManager = DBManager(connect_params)
db.insert_company("K-test")
db.insert_vacancy(
    title="py",
    salary=100,
    url="ddddd",
    description="fffff",
    company_name="K-test"
)

db.insert_vacancy(
    title="py2",
    salary=200,
    url="ddddd",
    description="fffff",
    company_name="K-test"
)
for name, count in db.get_companies_and_vacancies_count():
    print(f"{name}: {count} вакансий")
print("----------")
print(db.get_all_vacancies())
print("----------")
print(db.get_avg_salary())
print("----------")
print(db.get_vacancies_with_higher_salary())