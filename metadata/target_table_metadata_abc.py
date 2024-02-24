from abc import ABC, abstractmethod


class TargetTableMetadata(ABC):

    @property
    @abstractmethod
    def schema_name(self) -> str:
        pass

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    @property
    @abstractmethod
    def table_column_name_list(self) -> list[str]:
        pass

    @property
    @abstractmethod
    def insert_table_column_name_list(self) -> list[str]:
        pass
