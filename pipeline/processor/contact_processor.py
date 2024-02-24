from abc import abstractmethod, ABC


class EntityProcessor(ABC):

    @abstractmethod
    def get_cleaned_data(self) -> list[tuple]:
        pass

class ContactProcessor(EntityProcessor):

    def __init__(self):
        self.__cleaned_data: list[tuple] = list()


    def process_data(self, data: dict) -> None:
        pass