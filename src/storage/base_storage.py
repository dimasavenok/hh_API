import json
from abc import ABC, abstractmethod
from typing import List, Dict, Union

from src.models.vacancy import Vacancy


class BaseStorage(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict[str, Union[str, float]]]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass