class Vacancy:
    """Класс вакансий, добавляемых из списка словарей"""

    __slots__ = ("name", "salary", "url", "employer", "id")

    def __init__(self, vacancy):
        self.name = vacancy["name"]
        if vacancy["salary"]:
            self.salary = vacancy["salary"]["from"]
        else:
            self.salary = "не указана"
        self.url = vacancy["url"]
        self.employer = vacancy["employer"]["name"]
        self.id = vacancy["id"]

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        else:
            print("Вы пытаетесь сравнить объекты разных классов")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            print("Вы пытаетесь сравнить объекты разных классов")

    def __repr__(self):
        return f'{{"name": "{self.name}", "salary": {self.salary}, "url": "{self.url}", "employer": "{self.employer}", "id": {self.id}}}'
