
from database.postgres_db import PostgresDatabase


class DatabaseOperations:

    def __init__(self):
        self.__postgres: PostgresDatabase = PostgresDatabase()

    def get_data(self, schema_name: str, table_name: str, column_name_list: list[str], param: str = None,
                 param_data: tuple = None) -> list[dict]:
        try:
            column_names: str = ",".join(column_name_list)
            query: str = f"""Select {column_names} from {schema_name}.{table_name}"""
            if param:
                query += """ where """ + param
            self.__postgres.create_db_connection()
            return self.__postgres.get_data(query=query, param=param_data)
        finally:
            self.__postgres.close_db_connection()

    def get_data_with_custom_query(self, custom_query: str, param_data: tuple = None) -> list[dict]:
        try:
            self.__postgres.create_db_connection()
            return self.__postgres.get_data(query=custom_query, param=param_data)
        finally:
            self.__postgres.close_db_connection()

    def insert_data_to_db(self, schema_name: str, table_name: str, table_column_name_list: list[str],
                          param_data: list[tuple]) -> None:
        try:
            column_name_list: str = ", ".join(table_column_name_list)
            parameters = ", ".join(["%s"] * len(table_column_name_list))
            query: str = f"""insert into {schema_name}.{table_name}({column_name_list}) Values ({parameters})"""
            self.__postgres.create_db_connection()
            self.__postgres.insert_data(query=query, param_data=param_data)
            self.__postgres.commit_data()
        finally:
            self.__postgres.close_db_connection()
