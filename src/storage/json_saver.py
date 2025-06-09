import json
from typing import List, Dict, Union

from src.models.vacancy import Vacancy


class JSONSaver():
    __slots__ = ("filename",)


    def __init__(self, filename: str = "vacancies.json") -> None:
        self.filename = filename


    def __read_file(self) -> List[Dict[str, Union[str, float]]]:
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            self.__write_file(data=[])
            return []


    def __write_file(self, data: List[Dict[str, Union[str, float]]]) -> None:
        with open(self.filename, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)



    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        return self.__read_file()


    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies: List[Dict[str, Union[str, float]]] = self.get_all()
        vacancies.append(vars(vacancy))
        self.__write_file(vacancies)


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        # old_vacancies: List[Dict[str, Union[str, float]]] = self.get_all()
        # vacancies: List[Dict[str, Union[str, float]]] = [v for v in old_vacancies if v["vacancy_id"] != vacancy.vacancy_id]
        self.__write_file([v for v in self.get_all() if v["vacancy_id"] != vacancy.vacancy_id])