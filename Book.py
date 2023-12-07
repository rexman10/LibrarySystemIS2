class Book:
    def __init__(self, code, title, author, availability):
        self.code = code
        self.title = title
        self.author = author
        self.availability = availability
        
        
    def __str__(self):
        return f"Book{{code='{self.code}', title='{self.title}', author='{self.author}', availability={self.availability}}}"