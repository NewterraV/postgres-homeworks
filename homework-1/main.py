"""Скрипт для заполнения данными таблиц в БД Postgres."""
from src.classes.work_file import WorkSCV
from src.classes.work_bd import WorkBDLocal
import os

if __name__ == "__main__":

    database_name = 'north'
    tables = [{'table': 'employees', 'filename': 'employees_data.csv'},
              {'table': 'customers', 'filename': 'customers_data.csv'},
              {'table': 'orders', 'filename': 'orders_data.csv'}]

    user_password = input('Введите пароль для доступа к локальной базе данных')

    for table in tables:
        filename = os.path.join(os.path.abspath('north_data'), table['filename'])
        data = WorkSCV(filename)
        database = WorkBDLocal(database_name, user_password)
        database.write_bd(data.read_to_dict(), table['table'])

    print('Запись в базу данных выполнена успешно')
