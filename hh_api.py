import json
from api import API
import requests as rq
from pprint import pprint


class HH_API(API):
    hh_api = 'https://api.hh.ru/vacancies'

    def get_api(self, filter: str, quant = 100, page=0):
        params = {
            'text': f'NAME:{filter}',  # Текст фильтра.
            'area': 2,  # Поиск осуществляется по вакансиям города Санкт-петербург
            'page': page,  # Индекс страницы поиска на HH
            'per_page': quant  # Кол-во вакансий на 1 странице
        }
        req = rq.get(self.hh_api, params)  # Посылаем запрос к API
        return req.json()['items']


hh = HH_API()

#pprint(hh.get_api('Python Junior'))


