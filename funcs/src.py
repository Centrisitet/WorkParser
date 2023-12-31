from classes.hh_api import HH_API
from classes.sj_api import SuperJobApi
from classes.saver import Saver
from classes.vacancy import Vacancy


def get_vacancies(platform: int):
    """Основная функция, которая подключается к апи двух сайтов и сохраняет их в общий json файл"""
    hh = HH_API()
    sj = SuperJobApi()
    saver = Saver("../data.json")
    filter = input('Введите слово-фильтр: ')
    if platform == 1:
        for el in hh.get_api(filter):
            vac_hh = Vacancy(title=el['name'], url=el['alternate_url'], salary=el['salary'],
                             requirement=el['snippet']['requirement'])
    elif platform == 2:
        for el in sj.get_api(filter):
            salary = {'from': el['payment_from'], 'to': el['payment_to']}
            vac_sj = Vacancy(title=el['profession'], salary=salary, url=el["client"]["link"], requirement=el["candidat"])
    elif platform == 3:
        for el in hh.get_api(filter):
            vac_hh = Vacancy(title=el['name'], url=el['alternate_url'], salary=el['salary'],
                             requirement=el['snippet']['requirement'])
        for el in sj.get_api(filter):
            salary = {'from': el['payment_from'], 'to': el['payment_to']}
            vac_sj = Vacancy(title=el['profession'], salary=salary, url=el["client"]["link"], requirement=el["candidat"])
    else:
        print('Введено некорректное значение!')
        exit()
    saver.save_vacancies(Vacancy.vacs)
    return saver.load_vacancies()
