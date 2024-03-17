from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Docx reader"""
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot DocX ingest exception')
        
        quotes = []

        doc = docx.Document(path)
      
        for para in doc.paragraphs:
            if para.text != '':
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes