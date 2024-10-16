from src.api import HeadHunterApi
from src.files import JsonData
from src.vacanсies import Vacancy
from src.interface import get_vacancies, saved_vacancions

def main():
    user_answer = input('Желаете посмотреть актуальные или сохранённые вакансии? ')
    if user_answer.lower() == 'актуальные':
        name = input('По какой профессии ищете вакансии? ')
        number = int(input('Сколько вакансий вам показать? '))
        get_vacancies(name, number)
    elif user_answer.lower() == 'сохранённые':
        filename = input('Из какого файла желаете посмотреть вакансии? ')
        saved_vacancions(filename)

if __name__ == "__main__":
    main()