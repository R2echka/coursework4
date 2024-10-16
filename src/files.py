import json
from abc import ABC, abstractmethod


class BasicData(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def read_json():
        pass

    @abstractmethod
    def add_to_file():
        pass

    @abstractmethod
    def delete_from_file():
        pass


class JsonData(BasicData):
    """Класс для работы с json-файлами"""

    def __init__(self, filename="vacancies"):
        self.__filename = f"data/{filename}.json"

    def read_json(self):
        try:
            with open(self.__filename, encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_to_file(self, vacancy):
        with open(self.__filename, "a", encoding="utf-8") as file:
            json.dump(str(vacancy), file, indent=4, ensure_ascii=False)


    def delete_from_file(self, id):
        data = self.read_json()
        for vacancy in data:
            if vacancy["id"] == id:
                data.remove(vacancy)
        with open(self.__filename, "w") as file:
            json.dump(data, file)
