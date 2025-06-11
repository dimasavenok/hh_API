import json
from typing import List, Dict, Union

from src.models.vacancy import Vacancy
from src.storage.base_storage import BaseStorage


class JSONSaver(BaseStorage):
    def __init__(self, filename: str = "vacancies.json") -> None:
        super().__init__()


    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        return self._BaseStorage__read_file()


    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies: List[Dict[str, Union[str, float]]] = self.get_all()
        vacancies.append(vars(vacancy))
        self._BaseStorage__write_file(vacancies)


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        # old_vacancies: List[Dict[str, Union[str, float]]] = self.get_all()
        # vacancies: List[Dict[str, Union[str, float]]] = [v for v in old_vacancies if v["vacancy_id"] != vacancy.vacancy_id]
        self._BaseStorage__write_file([v for v in self.get_all() if v["vacancy_id"] != vacancy.vacancy_id])