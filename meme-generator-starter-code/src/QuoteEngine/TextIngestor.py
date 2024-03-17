from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Text reader"""

    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot TEXT ingest exception')
            
        quotes = []

        with open(path, "r", encoding='utf-8-sig') as t:
            for index, line in enumerate(t):
                parsed = line.strip().split('-')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)
                
        return quotes