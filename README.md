# Парсинг вакансий по выбранным компаниям на HH.RU и работа с данными через PostgreSQL

## Описание
Программа использует API HeadHunter для получения информации о вакансиях и компаниях. После получения данных, они сохраняются в базу данных PostgreSQL

## Установка
1. Скачайте проект в домашнюю директорию.
2. Активируйте виртуальное окружение командой: poetry shell.
3. Установите зависимости командой: poetry install.

## Перед первым запуском программы:

Создайте файл database.ini в папке src и заполните информацию в следующем формате:

[postgresql]<br />host=localhost<br />user=your_username<br />password=your_password 


## Работа кода

При запуске main.py будет произведен поиск вакансий компаний(Яндекс, СБЕР, Тинькофф, SkyEng, OBI, WildBerries, ГазпромБанк, VK, Ozon и Альфа-банк) по их url-адресам. Компании с их айди, а также их вакансии(название компании, название вакансии, ссылка и заработная плата) будут сохранены в таблицы БД под названием "hh_db" под названием companies и vacancies.

Также программа запрашивает ввод ключевого слова, по которому будет выводит список вакансий, имеющие данное слово. Функция поиска вакансий по ключевому слову позволяет быстро фильтровать результаты и получать интересующую вакансию. 








