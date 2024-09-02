import os

from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.results import InsertOneResult


load_dotenv()


class Database_operations:
    """
    Класс для взаимодействия с БД MongoDB.

    Атрибуты:
    client - это класс клиента MongoDB, принимает адрес БД и его порт;
    db - это имя БД в MongoDB;

    user_collection - это имя коллекции Пользователей в БД;
    group_collection - это имя коллекции Групп в БД.

    Методы:
    insert_collection(self, collection, data, _datetime) - добавление записи(-ей);
    delete_db_elements(self) - удаление всех объектов БД;
    print_db_elements(self, name_collection) - вывод в консоль объектов БД по
    имени коллекции.
    """

    client = MongoClient(os.getenv('DB_IP', os.getenv('DB_PORT')))
    db = client[os.getenv('DB_NAME')]
    user_collection = db[os.getenv('DB_USERS_COLLECTION')]
    group_collection = db[os.getenv('DB_GROUPS_COLLECTION')]

    def insert_collection(
        self, collection: Collection,
            data: list[dict],
            _datetime: str) -> InsertOneResult:
        """
        Принимает на вход коллекцию, дату и сохраняет данные в MongoDB.
        """

        datetime_obj = {'datetime': _datetime}

        if len(data) == 1:
            data[0].update(datetime_obj)
            return collection.insert_one(data[0])

        data_many = [item.update(datetime_obj) for item in data]
        return collection.insert_many(data_many)

    def delete_db_elements(self) -> None:
        """
        Удаляет все объекты БД.
        """

        self.user_collection.delete_many({})
        self.group_collection.delete_many({})

    def print_db_elements(self, name_collection: str) -> None:
        """
        Принимает на вход название коллекции и Выводит в консоль объекты БД.
        Если объекты отсутствуют, то вывод будет пустым списком.
        """

        obj = self.db[name_collection]
        pprint(list(obj.find()))
