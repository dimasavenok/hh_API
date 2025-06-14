from typing import Any, Dict, List

import requests


from src.api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    def __init__(self) -> None:
       super().__init__()



    def get_vacancies(self, keyword: str) -> List[Dict[Any, Any]]:
        return self._BaseAPI__connect(keyword).json().get("items", [])
