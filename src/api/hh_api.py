from typing import Any, Dict, List

import requests


from src.api.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    __slots__ = ("__base_url", "__headers")

    def __init__(self) -> None:
        self.__base_url = 'https://api.hh.ru'
        self.__headers = {'User-Agent': 'HH-User-Agent'}


    def __connect(self, keyword: str) -> requests.Response:
        params: Dict[str, str | int] = {
            "text": keyword,
            "area": 1,
            "per_page": 100,
        }
        response: requests.Response = requests.get(f"{self.__base_url}/vacancies", headers=self.__headers,
                                                   params=params)
        response.raise_for_status()
        return response


    def get_vacancies(self, keyword: str) -> List[Dict[Any, Any]]:
        return self.__connect(keyword).json().get("items", [])
