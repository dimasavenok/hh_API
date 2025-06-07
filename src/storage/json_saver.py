import json
from typing import List, Dict, Union

from src.models.vacancy import Vacancy


class JSONSaver():
    def __init__(self, filename: str = "vacancies.json") -> None:
        self.filename = filename

    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.filename, mode="w", encoding="utf-8") as file:
                json.dump({}, file, ensure_ascii=False, indent=4)
            return []


    def add_vacancy(self, vacancy: Vacancy):
        vacancies: List[Dict[str, Union[str, float]]] = self.get_all()
        vacancies.append(vars(vacancy))
        with open(self.filename, mode="w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)


