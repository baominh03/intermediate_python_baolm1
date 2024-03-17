class QuoteModel():
    def __init__(self, body, author):
        """Model creation from Ingestor.

        :param body: content in CSV,DOCX,PDF,TEXT ingestor
        :param auter: author inCSV,DOCX,PDF,TEXT ingestor
        """
        
        self.body = body
        self.author = author

    def __repr__(self):
        """Return Quote Model"""
        return (f'{self.body} - {self.author}')