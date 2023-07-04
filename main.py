from funcs.src import get_vacancies

platform = int(input('''Введите желаемую платформу для поиска:
1. HH.ru
2. Superjob.ru
3. Обе
'''))
print(get_vacancies(platform))

