from config import config
import psycopg2


class DBManager:
    def __init__(self):
        self.params = config()
        self.conn = psycopg2.connect(database='hh_db', **self.params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """ Получает список всех компаний и количество вакансий у каждой компании."""

        query = ('SELECT company, COUNT(*) as count_vacs '
                 'FROM vacancies '
                 'GROUP BY company;')

        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def get_all_vacancies(self):
        """ Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""

        query = ('SELECT * '
                 'FROM vacancies;')
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям."""

        query = ('SELECT AVG(salary) '
                 'FROM vacancies;')
        self.cur.execute(query)
        result = int(self.cur.fetchone()[0])
        return result

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

        avg_salary = self.get_avg_salary()
        query = (f'SELECT * '
                 f'FROM vacancies '
                 f'WHERE salary > {avg_salary};')
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”."""

        query = (f'SELECT * '
                 f'FROM vacancies '
                 f"WHERE vacancy_name ILIKE '%{keyword}%';")
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def close_con(self):
        """Выключение подключения"""

        self.cur.close()
        self.conn.close()
