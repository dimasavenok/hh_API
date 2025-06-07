from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
    api = HeadHunterAPI()
    raw_vacancies = api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(raw_vacancies)

    json_saver = JSONSaver()
    for vacancy in vacancies:
        json_saver.add_vacancy(vacancy)
        print(vacancy)





if __name__ == "__main__":
    user_interaction()
