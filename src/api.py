from abc import ABC, abstractmethod

import requests


class BasicApi(ABC):
    """Абстрактный класс для работы с апи"""

    @abstractmethod
    def get_api():
        pass

    @abstractmethod
    def get_vacancies():
        pass


class HeadHunterApi(BasicApi):
    """Класс для работы с апи hh.ru"""

    def __init__(self, name, raiting):
        self.name = name
        self.url = "https://api.hh.ru/vacancies"
        self.params = {"text": self.name, "page": 0, "per_page": raiting}
        self.vacancies = []

    def get_api(self):
        return requests.get(self.url, params=self.params)

    def get_vacancies(self):
        response = self.get_api()
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")
            self.vacancies.append(vacancies)
            return self.vacancies
        else:
            return []

