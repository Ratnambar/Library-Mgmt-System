# -*- coding: utf-8 -*-
from Book import Book
#First Book is file & second is Class

class Catalog:
    def __init__(self):
        self.different_book_count = 0
        self.books = []
        
    #Only available to admin
    def addBook(self,name,author,publish_date,pages):
        b = Book(name,author,publish_date,pages)
        self.different_book_count += 1
        self.books.append(b)
        return b
    
    #Only available to admin
    def addBookItem(self,book,isbn,rack):
        book.addBookItem(isbn, rack)
        
        
    def checkIfBookExistsByName(self,name):
         book_by_name_exist = [book for book in self.books if book.name == name]
         if  book_by_name_exist:
             return book_by_name_exist
         else:
             return False
    
    def checkIfBookExistsByAuthor(self,author):
         book_by_author_exist = [book for book in self.books if book.author == author]
         if book_by_author_exist:
             return book_by_author_exist
         else:
             return False
         
    
    def checkIfBookIssuedByMember(self,book,librarian_id):
            if book.checkBookItemIssued(librarian_id):
                return True
            else:
                return False
        
    def searchByName(self,name):
        book_name_exist = Catalog.checkIfBookExistsByName(name)
        if book_name_exist:
            print('The book {} is present in library'.format(book_name_exist[-1].name))
            print('Author',book_name_exist[-1].author)
            print('Number of copies of this book in library:-',book_name_exist[-1].total_count)
        else:
            print('This book is not present in the library')
            
        

    def searchByAuthor(self,author):
       book_by_author_exist = Catalog.checkIfBookExistsByAuthor(author)
       if book_by_author_exist:
           print('Book by author {} is present in library '.format(book_by_author_exist[-1].author))
           print('Book Name',book_by_author_exist[-1].name)
           print('Number of copies of this book in library:-',book_by_author_exist[-1].total_count)
       else:
           print('This book is not present in the library')
           
        
    def displayAllBooks(self):
        print ('Different Book Count',self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        print ('Total Number of Book is : ',c)
        
        
    def setLibrarianForBookItem(self,book,librarian_id, librarian_name,issueDay):
        book.setLibrarianDetails(librarian_id, librarian_name,issueDay)
        
    
    def displayLibrarianDetails(self):
        print('The issued books are:-')
        for book in Catalog.books:
            book.printLibrarianDetails()
            
    
    def retunBookUpdateCatalog(self,book,librarian_id):
        book.retunBookUpdateBookItem(librarian_id)
