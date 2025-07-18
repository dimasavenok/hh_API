from typing import List

from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.DBManager import DBManager
from src.storage.json_saver import JSONSaver
from src.untils.helpers import filter_vacancies_by_keywords, filter_vacancies_by_salary, get_top_vacancies


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n: int = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words: List[str] = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range: str = input("Введите диапазон зарплат(Пример: 100000 - 150000): ")
    api = HeadHunterAPI()
    raw_vacancies = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(raw_vacancies)

    json_saver = JSONSaver(filename="data/no_filtred_vacancies.json")
    for vacancy in vacancies:
        json_saver.add_vacancy(vacancy)

    connect_params = {
        "dbname": "hh_db",
        "user": "postgres",
        "password": "dima510141",
        "host": "localhost",
        "port": "5432"
    }
    DBManager.create_database({"user": "postgres",
        "password": "dima510141",
        "host": "localhost",
        "port": "5432"}, "hh_db")
    db: DBManager = DBManager(connect_params)
    for i, vacancy in enumerate(vacancies):
        if i == 10:
            break
        db.insert_vacancy(
            title=vacancy.title,
            salary=vacancy.salary,
            url=vacancy.url,
            description=vacancy.description,
            company_name=vacancy.employer
        )


    filtered = filter_vacancies_by_keywords(vacancies, filter_words)
    ranged = filter_vacancies_by_salary(filtered, salary_range)
    top = get_top_vacancies(ranged, top_n)

    print("\nТоп вакансий:\n")
    json_saver = JSONSaver(filename="data/vacancies.json")
    for vacancy in top:
        print(vacancy)
        json_saver.add_vacancy(vacancy)



if __name__ == "__main__":
    user_interaction()
