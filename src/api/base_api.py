from abc import ABC, abstractmethod
from typing import Any, List, Dict


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict[Any, Any]]:
        pass
