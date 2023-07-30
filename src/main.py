from DBManager import DBManager
from utils import *


def main():
    # Создание БД
    params = config()
    create_database('hh_db', params)

    # Получение информации по компаниям
    fill_in_database('https://api.hh.ru/vacancies?employer_id=1740')  # Компания Яндекс
    fill_in_database('https://api.hh.ru/vacancies?employer_id=3529')  # Компания СБЕР
    fill_in_database('https://api.hh.ru/vacancies?employer_id=78638')  # Компания Тинкофф
    fill_in_database('https://api.hh.ru/vacancies?employer_id=1122462')  # Компания Skyeng
    fill_in_database('https://api.hh.ru/vacancies?employer_id=1634')  # Компания OBI
    fill_in_database('https://api.hh.ru/vacancies?employer_id=87021')  # Компания WildBerries
    fill_in_database('https://api.hh.ru/vacancies?employer_id=3388')  # Компания ГазпромБанк
    fill_in_database('https://api.hh.ru/vacancies?employer_id=15478')  # Компания VK
    fill_in_database('https://api.hh.ru/vacancies?employer_id=2180')  # Компания Ozon
    fill_in_database('https://api.hh.ru/vacancies?employer_id=80')  # Компания Альфа-Банк

    # Подключение к классу, который подключается к БД PostgreSQL
    database = DBManager()

    # Вывод компаний и число их вакансий
    companies_and_vacs = database.get_companies_and_vacancies_count()
    print(f'Компании и количество вакансий: {companies_and_vacs}')

    # Вывод всех вакансий
    all_vacancies = database.get_all_vacancies()
    print(f'Все вакансии : {all_vacancies}')

    # Вывод средней зарплаты
    avg_salary = database.get_avg_salary()
    print(f'Средняя зарплата: {avg_salary} руб.')

    # Вывод вакансий с зарплатой выше средней
    higher_avg_salary = database.get_vacancies_with_higher_salary()
    print(f'Вакансии с зарплатой выше средней: {higher_avg_salary}')

    # Поиск вакансий по ключевому слову
    keyword = input('Введите ключевое слово для поиска вакансии: ')
    vacancies_with_keyword = database.get_vacancies_with_keyword(keyword)
    print(f'Вакансии по ключевому слову: {vacancies_with_keyword}')

    # Отключение от БД
    database.close_con()


if __name__ == '__main__':
    main()
