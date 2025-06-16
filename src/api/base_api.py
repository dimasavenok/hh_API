from abc import ABC, abstractmethod
from typing import Any, List, Dict

import requests



class BaseAPI(ABC):
    def __connect(self, keyword: str) -> requests.Response:
        pass


    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict[Any, Any]]:
        pass
