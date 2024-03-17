from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    This class should define two methods with the following class method signatures:  

   def can_ingest(cls, path) -> boolean
   def parse(cls, path: str) -> List[QuoteModel] 
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """To verify ingestible"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To Parse to QuoteModel"""
        pass