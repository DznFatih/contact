import psycopg2

from database.config import Config
from database.database_interface import Database
from exception.custom_exceptions import DBConnectionNotSet


class PostgresDatabase(Database):

    def __init__(self):
        self.__config: dict = dict()
        self.__db_connection: psycopg2.connection = None

    def create_db_connection(self) -> None:
        self.__config = Config.get_dwh_config()
        self.__db_connection: psycopg2.connection = psycopg2.connect(host=self.__config["host"],
                                                                     database=self.__config["database"],
                                                                     user=self.__config["user"],
                                                                     password=self.__config["password"])

    def get_data(self, query: str, param: tuple = None) -> list[dict]:
        if self.__db_connection is None:
            raise DBConnectionNotSet
        cur = self.__db_connection.cursor()
        if param:
            cur.execute(query=query, vars=param)
        else:
            cur.execute(query=query)
        data: list[dict] = self.__make_dict(cursor=cur)
        cur.close()
        return data

    def insert_data(self, query: str, param_data: list[tuple]) -> None:
        if self.__db_connection is None:
            raise DBConnectionNotSet
        cur = self.__db_connection.cursor()
        cur.executemany(query=query, vars_list=param_data)
        cur.close()

    @staticmethod
    def __make_dict(cursor) -> list[dict]:
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results

    def close_db_connection(self) -> None:
        if self.__db_connection is not None:
            self.__db_connection.close()

    def commit_data(self) -> None:
        if self.__db_connection is not None:
            self.__db_connection.commit()

    def roll_back(self) -> None:
        self.__db_connection.rollback()

# p = PostgresDatabase()
# data = p.get_data(query="""Select *
# from contact.contacts where id in (%s) """, param=(1,))
# print(data)