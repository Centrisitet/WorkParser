import json
from vacancy import Vacancy


class Saver:
    """Класс, который сохраняет все вакансии в json файл."""

    def __init__(self, path):
        self.__path = path

    def __save_data(self, data):
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(data, f, sort_keys=False, indent=2, ensure_ascii=False)

    def __load_data(self):
        with open(self.__path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def save_vacancies(self, vacancies):
        vacancies_data = []
        for el in vacancies:
            vacancies_data.append(el.as_dict())
        self.__save_data(vacancies_data)

    def load_vacancies(self):
        dict_vacancies = self.__load_data()
        vacancies = []
        for el in dict_vacancies:
            new_vac = Vacancy(el['title'], el['url'], el['salary_min'], el['salary_max'], el['requirement'])
            vacancies.append(new_vac)
        return vacancies