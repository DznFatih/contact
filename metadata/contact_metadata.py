from metadata.target_table_metadata_abc import TargetTableMetadata


class ContactMetadata(TargetTableMetadata):
    @property
    def schema_name(self) -> str:
        return "contact"

    @property
    def table_name(self) -> str:
        return "contacts"

    @property
    def table_column_name_list(self) -> list[str]:
        return ["ID", "Name", "PhoneNumber", "Notes"]

    @property
    def insert_table_column_name_list(self) -> list[str]:
        return ["Name", "PhoneNumber", "Notes"]
