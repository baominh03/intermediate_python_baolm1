from QuoteEngine.QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from typing import List


class Ingestor(IngestorInterface):
    """Inherit from IngestorInterface.py"""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parsing to QuoteModel"""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)