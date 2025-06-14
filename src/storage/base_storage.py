import json
from abc import ABC, abstractmethod
from typing import List, Dict, Union

from src.models.vacancy import Vacancy


class BaseStorage(ABC):
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

    @abstractmethod
    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass