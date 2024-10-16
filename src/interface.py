from src.api import HeadHunterApi
from src.files import JsonData
from src.vacanсies import Vacancy

def get_vacancies(vacancy, per_page):
    '''Работа с новыми для пользователя вакансиями'''
    vacancies = HeadHunterApi(vacancy, per_page)
    if vacancies.get_vacancies() != [[]]:
        for vacancy in vacancies.get_vacancies()[0]:
            vac = Vacancy(vacancy)
            print(f'{vac.name}, зарплата: {vac.salary}, наниматель: {vac.employer}, id: {vac.id}')
            saving = input('Желаете сохранить вакансию?(Да/Нет) ')
            if saving.lower() == 'да':
                filename = input('Введите название файла для сохранения(на английском) ')
                if filename != '':
                    file = JsonData(filename)
                else:
                    file = JsonData()
                file.add_to_file(vac)
            else:
                continue
    else:
        print('По вашему запросу не найдено вакансий')

def saved_vacancions(filename='vacancies'):
    '''Работа с сохранёнными ранее вакансиями'''
    file = JsonData(filename)
    print(file.read_json())
    quest = input('Желаете что-либо удалить? ')
    if quest.lower() == 'да':
        id = input('Введите id вакансии ')
        file.delete_from_file(id)