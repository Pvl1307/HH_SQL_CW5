 -- Команды для работы с БД и таблицами

DROP DATABASE hh_db;
CREATE DATABASE hh_db;

CREATE TABLE companies (
        company_id INT,
        company VARCHAR PRIMARY KEY NOT NULL
);

CREATE TABLE vacancies (
        company VARCHAR REFERENCES companies(company) NOT NULL,
        vacancy_name VARCHAR NOT NULL,
        vacancy_url TEXT,
        salary INT
);


INSERT INTO companies (company_id, company) VALUES (%s, %s);

INSERT INTO vacancies (company, vacancy_name, vacancy_url, salary) VALUES (%s, %s, %s, %s);


SELECT company, COUNT(*) as count_vacs FROM vacancies GROUP BY company;

SELECT * FROM vacancies;

SELECT AVG(salary) FROM vacancies;

SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies);

SELECT * FROM vacancies WHERE vacancy_name ILIKE '%s';