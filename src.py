from hh_api import HH_API
from sj_api import SuperJobApi
from saver import Saver
from vacancy import Vacancy


def main():
    hh = HH_API()
    sj = SuperJobApi()
    saver = Saver("data.json")
    filter = input('Введите слово-фильтр: ')
    try:
        for el in hh.get_api(filter):
            vac_hh = Vacancy(el['name'], el['salary']['from'], el['salary']['to'], el['alternate_url'],
                                     el['snippet']['requirement'])
            print(el)
            print(Vacancy.vacs)
        saver.save_vacancies(Vacancy.vacs)
        print(saver.load_vacancies())

        for el in sj.get_api(filter):
            vac_sj = Vacancy(el['profession'], el["payment_from"], el["payment_to"], el["client"]["link"],
                             el["candidat"])
            saver.save_vacancies([vac_sj])
        print(saver.load_vacancies())
    except KeyError:
        print('KeyError ')
    except TypeError:
        print('TypeError ')


if __name__ == "__main__":
    main()