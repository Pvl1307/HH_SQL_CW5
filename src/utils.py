from typing import Any
from API_connection import get_vacancies
import psycopg2
import requests
from config import config


def get_vacancies_by_company_url(url: str):
    """Получение вакансий через URL компании"""

    response = requests.get(url, params={'per_page': 100, 'only_with_salary': 'true'})
    if response.status_code == 200:
        vacancies = response.json().get('items')
    else:
        print('Ошибка подключения к вакансиям')

    return vacancies


def create_database(database_name: str, params: dict) -> None:
    """Создание БД и таблиц для сохранения данных"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE companies (
                    company_id INT,
                    company VARCHAR PRIMARY KEY NOT NULL
                    )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    company VARCHAR REFERENCES companies(company) NOT NULL,
                    vacancy_name VARCHAR NOT NULL,
                    vacancy_url TEXT,
                    salary INT
                    )
            """)

    conn.commit()
    conn.close()


def fill_company_table(data: list[dict[str, Any]], db_name: str, params: dict) -> None:
    """Заполнение таблицы компаний"""

    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        company_id = data[0].get('employer').get('id')
        company_name = data[0].get('employer').get('name')

        cur.execute("""INSERT INTO  companies (company_id, company) 
        VALUES (%s, %s)""", (company_id, company_name))

    conn.commit()
    conn.close()


def fill_vacancies_table(data: list[dict[str, Any]], db_name: str, params: dict) -> None:
    """Заполнение таблицы вакансий"""

    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        for vac in data:
            company_name = vac.get('employer').get('name')
            vac_name = vac.get('name')
            vac_url = vac.get('alternate_url')
            salary_from = vac.get('salary').get('from')
            salary_to = vac.get('salary').get('to')

            if salary_from is None:
                salary_from = salary_to
            elif salary_from is None and salary_to is None:
                salary_from = 0

            cur.execute(
                """INSERT INTO vacancies (company, vacancy_name, vacancy_url, salary) 
                VALUES (%s, %s, %s, %s)""",
                (company_name, vac_name, vac_url, salary_from))

    conn.commit()
    conn.close()


def fill_in_database(company_url) -> None:
    """Запись в PostgreSQL"""

    params = config()
    info = get_vacancies_by_company_url(company_url)
    fill_company_table(info, 'hh_db', params)
    fill_vacancies_table(info, 'hh_db', params)
