from abc import ABC, abstractmethod


class API(ABC):
    '''
    Абстрактный класс для работы с апи
    '''
    @abstractmethod
    def get_api(self, api):
        pass