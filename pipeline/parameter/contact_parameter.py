from abc import ABC

from metadata.contact_metadata import ContactMetadata
from metadata.target_table_metadata_abc import TargetTableMetadata


class EntityParameter(ABC):
    pass

class EntityProcessor(ABC):
    pass



class ContactParameter(EntityParameter):

    def __init__(self) -> None:
        self.__contact_metadata: TargetTableMetadata = ContactMetadata()
        self.__data_processor: EntityProcessor = ContactProcessor()

