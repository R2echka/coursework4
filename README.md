# Курсовой проект по 4 модулю
### Описание:
Программа, позволяющая сохранять и удобно работать с информацией с сайта hh.ru

## Класс для работы с api
Находится в файле [`api.py`](src/api.py)
### Методы
+ `get_api` - Подключение к api сервиса
+ `get_vacancies` - Получение информации по интересующей пользователя профессии

## Класс для работы с вакансиями
Находится в файле [`vacancies.py`](src/vacancies.py)

## Класс для работы с файлами
Находится в файле [`files.py`](src/files.py)
### Методы
+ `read_json` - Получение информации из ранее сохранённого файла
+ `add_to_file` - Добавление информации о профессии в файл
+ `delete_from_file` - Удаление информации о профессии из файла

## Дополнительные функции
Код находится в файле [`interface.py`](src/interface.py)
### Функции
+ `get_vacancies` - Работа с новыми для пользователя вакансиями
+ `saved_vacancies` - Работа с сохранёнными ранее вакансиями

## Главный файл проекта
Код находится в файле [`main.py`](main.py)
### Функции
+ `main` - Основная функция, объединяющая все главные функции остальных файлов