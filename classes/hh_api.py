from api import API
import requests as rq


class HH_API(API):
    """Класс для работы с апи ХХ"""
    hh_api = 'https://api.hh.ru/vacancies'

    def get_api(self, filter: str, quant = 100, page=0):
        """Метод для получения вакансий с хх, по городу СПБ, фильтр по названию вводит юзер"""
        params = {
            'text': f'NAME:{filter}',  # Текст фильтра.
            'area': 2,  # Поиск осуществляется по вакансиям города Санкт-петербург
            'page': page,  # Индекс страницы поиска на HH
            'per_page': quant  # Кол-во вакансий на 1 странице
        }
        req = rq.get(self.hh_api, params)  # Посылаем запрос к API
        return req.json()['items']