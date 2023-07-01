class Vacancy:
    vacs = []

    def __init__(self, title, url, salary, requirement):
        self.title = title
        self.url = url
        self.salary_min = None
        self.salary_max = None
        if isinstance(salary, dict):
            self.salary_min = salary['from']
            self.salary_max = salary['to']
        self.requirement = requirement
        Vacancy.vacs.append(self)

    def __str__(self):
        return f"{self.title}, {self.url}, {self.salary_min}, {self.salary_max}, {self.requirement}"

    def __repr__(self):
        return f'Название: {self.title}, URL: {self.url}, Зарплата от {self.salary_min} до {self.salary_max}, Требования: {self.requirement}'

    '''
    Метод для перевода экземпляра вакансии в вид словаря
    '''
    def as_dict(self):
        vacancy = {"title": self.title,
                   "url": self.url,
                   "salary_min": self.salary_min,
                   "salary_max": self.salary_max,
                   "requirement": self.requirement
                   }
        return vacancy
