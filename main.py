from database.database_operations import DatabaseOperations
from metadata.contact_metadata import ContactMetadata
from metadata.target_table_metadata_abc import TargetTableMetadata


def get_contacts() -> list[dict]:
    contact_metadata: TargetTableMetadata = ContactMetadata()
    db_operations: DatabaseOperations = DatabaseOperations()
    return db_operations.get_data(schema_name=contact_metadata.schema_name,
                                  table_name=contact_metadata.table_name,
                                  column_name_list=contact_metadata.table_column_name_list)


def insert_contacts(param_data: list[tuple]) -> None:
    contact_metadata: TargetTableMetadata = ContactMetadata()
    db_operations: DatabaseOperations = DatabaseOperations()
    db_operations.insert_data_to_db(schema_name=contact_metadata.schema_name,
                                    table_name=contact_metadata.table_name,
                                    table_column_name_list=contact_metadata.insert_table_column_name_list,
                                    param_data=param_data)


if __name__ == "__main__":
    try:
        print(insert_contacts([("Radvi", "12345", None)]))

    except KeyError as e:
        print(str(e))
    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
