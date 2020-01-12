# -*- coding: utf-8 -*-
from BookItem import BookItem

class Book:
    def __init__(self,name,author,publish_date,pages):
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.book_item = []
        self.Book_Issuer_Details = []
        
    def addBookItem(self,isbn,rack):
        b = BookItem(self, isbn, rack, librarian_id = 0, librarian_name = '',issueDay = 0)
        self.book_item.append(b)
        self.total_count +=1
        
    def setLibrarianDetails(self, Librarian_id, Librarian_name, IssueDays):
       book_issue = [book for book in self.book_item if book.librarian_id == 0]
       if book_issue:
           book_issue[0].setLibrarianDetails(Librarian_id, Librarian_name, IssueDays)
       else:
           print('All copies of this book are issued')
        
        
    def checkBookItemIssued(self,issuer_id):
        book_issue = [book for book in self.book_item if book.librarian_id == librarian_id]
        if book_issue:
            return True
        else:
            return False
        
        
    def retunBookUpdateBookItem(self,librarian_id):
        book_issue = [book for book in self.book_item if book.librarian_id == librarian_id]
        if book_issue:
            issueDay = 0
            librarian_name = ''
            librarian_id = 0
            book_issue[0].setLibrarianDetails(librarian_id, librarian_name,issueDay) 
    
    
    def printBook(self):
        print (self.name,self.author)
        for book_item in self.book_item:
            if book_item.librarian_name == '':
                 print ('Book Id-{} Issued by - None'.format(book_item.isbn))
            else:
                print ('Book Id-{} Issued by - {}'.format(book_item.isbn, book_item.librarian_name))
    
    
    def printLibrarianDetails(self):
        for book in self.book_item:
            if book.librarian_id != 0:
                print('Book Name: {}  | Issuer Name - {} | Days Issued = {}'.format(self.name,book.librarian_id, book.issueDay))
