from database.postgres_db import PostgresDatabase


class DatabaseOperations:

    def __init__(self):
        pass

    def get_data(self, schema_name: str, table_name: str, column_name_list: list[str], param: str = None,
                 param_data: tuple = None) -> list[dict]:

        column_names: str = ",".join(column_name_list)
        query: str = f"""Select {column_names} from {schema_name}.{table_name}"""
        if param:
            query += """ where """ + param
        p = PostgresDatabase()
        return p.get_data(query=query, param=param_data)

    def get_data_with_custom_query(self, custom_query: str) -> list[dict]:
        pass

