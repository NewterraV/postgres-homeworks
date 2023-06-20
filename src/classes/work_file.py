from abc import ABC, abstractmethod
import csv


class WorkFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def read_to_dict(self):
        """Функция считывает данные из файла и на их основе возвращает список словарей"""
        pass


class WorkSCV(WorkFile):
    """Класс для работы с файлами формата SCV"""

    def __init__(self, filename: str):
        self.filename = filename

    def read_to_dict(self) -> list:

        with open(self.filename, 'r', encoding='utf8') as f:
            csv_items = csv.DictReader(f)
            data = []
            for i in csv_items:
                item_dict = {}
                for keys, values in i.items():
                    item_dict[keys] = values
                data.append(item_dict)
            return data
