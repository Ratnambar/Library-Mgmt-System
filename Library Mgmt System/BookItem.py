# -*- coding: utf-8 -*-
class BookItem:
    bkItem = []
    def __init__(self,book,isbn,rack,librarian_id,librarian_name,issueDay):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.librarian_id = librarian_id
        self.librarian_name = librarian_name
        self.issueDay = issueDay
        BookItem.bkItem.append(self)
        
        
    def setLibrarianDetails(self,Librarian_id,Librarian_name,IssueDays):
        self.librarian_id = Librarian_id
        self.librarian_name = Librarian_name
        self.issueDay = IssueDays
        
        
