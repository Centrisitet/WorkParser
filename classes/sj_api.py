import requests as rq
from api import API
from pprint import pprint


class SuperJobApi(API):
    """Класс для подключения к API superjob.ru"""
    def __init__(self):
        self.api_url = "https://api.superjob.ru/2.0/vacancies/"
        self.headers = {"Host": "api.superjob.ru",
                        "X-Api-App-Id": "v3.r.137564147.440d6445f074b79c9f533e748a1ca9cfc89be8d6.eb9b16cee82f3151099f3b44fb98ea669e82a13b",
                        "Authorization": "Bearer r.000000010000001.example.access_token",
                        "Content-Type": "application/x-www-form-urlencoded"
                        }

    def get_api(self, filter: str):
        """Метод для получения вакансий с СЖ с фильтром по названию. Фильтр вводит юзер"""
        params = f'?keyword={filter}&period=3'
        """Метод для получения вакансий """
        req = rq.get(self.api_url+params, headers=self.headers)
        return req.json()['objects']
