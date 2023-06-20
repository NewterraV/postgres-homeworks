import psycopg2
from abc import ABC, abstractmethod


class WorkBD(ABC):
    """Класс для работы с базами данных"""
    @abstractmethod
    def write_bd(self, data: dict, table_name: str):
        """Метод выполняет запись в базу данных"""
        pass


class WorkBDLocal(WorkBD):

    def __init__(self, database, password, host='localhost', user='postgres',):
        self.database = database
        self.password = password
        self.host = host
        self.user = user

    def write_bd(self, data: list, table_name: str):

        con = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        try:
            with con:
                with con.cursor() as cur:

                    for i in data:
                        items = []
                        for keys, values in i.items():
                            items.append(values)
                        number_values = len(items)
                        format_values = "%s, " * number_values
                        cur.execute(f'INSERT INTO {table_name} VALUES ({format_values[:-2]})', tuple(items))

        finally:
            con.close()
