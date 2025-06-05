from abc import ABC, abstractmethod
from typing import Any


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str) -> Any:
        pass
