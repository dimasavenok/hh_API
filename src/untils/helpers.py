from typing import List

from src.models.vacancy import Vacancy


def filter_vacancies_by_keywords(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    return [
        v for v in vacancies
        if v.description and any(word.lower() in v.description.lower() for word in keywords)
    ]


def filter_vacancies_by_salary(vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    min_salary, max_salary = map(int, salary_range.replace(" ", "").split("-"))
    # min_salary, max_salary = [int(num) for num in salary_range.replace(" ", "").split("-")]
    return [
        v for v in vacancies
        if min_salary <= v.salary <= max_salary
    ]


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    return sorted(vacancies, reverse=True)[:top_n]
