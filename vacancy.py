class Vacancy:
    vacs = []

    def __init__(self, title, url, salary_min, salary_max, requirement):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.requirement = requirement
        self.vacs.append(self)

    def __str__(self):
        return f"{self.title}, {self.url}, {self.salary_min}, {self.salary_max}, {self.requirement}"

    def __repr__(self):
        return f'Название: {self.title}, URL: {self.url}, Зарплата от {self.salary_min} до {self.salary_max}, Требования: {self.requirement}'

    def as_dict(self):
        vacancy = {"title": self.title,
                   "url": self.url,
                   "salary_min": self.salary_min,
                   "salary_max": self.salary_max,
                   "requirement": self.requirement


        }
        return vacancy



