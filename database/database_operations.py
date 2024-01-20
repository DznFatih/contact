import psycopg2

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
        except psycopg2.DatabaseError as e:
            print(str(e))
        except psycopg2.Error as e:
            print(str(e))
        except ValueError as e:
            print(str(e))
        except TypeError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
        finally:
            self.__postgres.close_db_connection()

    def get_data_with_custom_query(self, custom_query: str, param_data: tuple = None) -> list[dict]:
        try:
            self.__postgres.create_db_connection()
            return self.__postgres.get_data(query=custom_query, param=param_data)
        except psycopg2.DatabaseError as e:
            print(str(e))
        except psycopg2.Error as e:
            print(str(e))
        except ValueError as e:
            print(str(e))
        except TypeError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
        finally:
            self.__postgres.close_db_connection()


p = DatabaseOperations()
d = p.get_data("contact", "cc", column_name_list=["id"])
