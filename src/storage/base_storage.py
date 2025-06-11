from abc import ABC, abstractmethod
from typing import List, Dict, Union

from src.models.vacancy import Vacancy


class BaseStorage(ABC):
    @abstractmethod
    def __read_file(self) -> List[Dict[str, Union[str, float]]]:
        pass

    @abstractmethod
    def __write_file(self, data: List[Dict[str, Union[str, float]]]) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass