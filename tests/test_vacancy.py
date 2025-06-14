import pytest

from src.models.vacancy import Vacancy


def test_validate_salary():
    assert Vacancy.validate_salary({"from":50000}) == 50000
    assert Vacancy.validate_salary(None) == 0
    assert Vacancy.validate_salary({"to": 50000}) == 0


def test_cast_to_object_list():
    data = [
        {
            "id": "121434418",
            "name": "Frontend React разработчик",
            "alternate_url": "https://hh.ru/vacancy/121434418",
            "salary": {"from":50000},
            "snippet": {"requirement":"50000"}
        },
        {
            "id": "120881704",
            "name": "React developer middle+\\senior",
            "alternate_url": "https://hh.ru/vacancy/120881704",
            "salary": {"from":50000},
            "snippet": {"requirement":"50000"}
        }
    ]
    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 2
    assert vacancies[0].title == "Frontend React разработчик"
    assert vacancies[1].description == "50000"

