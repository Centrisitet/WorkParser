from src import main
from saver import Saver
from vacancy import Vacancy
from hh_api import HH_API
from sj_api import SuperJobApi
from pprint import pprint


hh = HH_API()
sj = SuperJobApi()

hh_data = hh.get_api('Python')
sj_data = sj.get_api('Python')

all_data = hh_data + sj_data

saver = Saver('jobs.json')
saver.save_vacancies(all_data)

pprint(all_data)



if __name__ == "__main__":
    main()