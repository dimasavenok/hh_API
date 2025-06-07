from typing import Any, Dict

import requests

from src.api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    def get_vacancies(self, keyword: str) -> Any:
        url: str = "https://api.hh.ru/vacancies"
        params: Dict[str, str | int] = {
            "text": keyword,
            "area": 1,
            "per_page": 100,
        }
        response: requests.Response = requests.get(url, params=params)
        return response.json().get("items", [])
