from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def get_data(self) -> list[dict]:
        pass


    @abstractmethod
    def insert_data(self) -> None:
        pass
