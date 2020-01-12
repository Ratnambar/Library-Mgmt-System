# -*- coding: utf-8 -*-
from Catalog import Catalog
from BookIssue import BookIssue


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.books = []
        

class Member(User):
    
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name, days=10):
        book_exist = Catalog.checkIfBookExistsByName(name)
        if book_exist:
            BookIssue.issueBook(book_exist[-1],self.student_id,self.name,days)
        else:
            print('Book is not available in library')
        
    #assume name is unique
    def returnBook(self,name,BookName):
        book_exist = Catalog.checkIfBookExistsByName(BookName)
        
        if book_exist:
            book_issued_by_user = Catalog.checkIfBookIssuedByMember(book_exist[0], self.student_id)
        
        if book_exist and  book_issued_by_user:
            BookIssue.returnBook(book_exist[0],self.student_id)
        else:
            print('This book is not present in library')
            
        
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        catalog = Catalog()
        b = catalog.addBook(name,author,publish_date,pages)
        return b
    
    def removeBook(self,name):
        #Check if the book by the given name exists
        book_name_exist = Catalog.checkIfBookExistsByName(name)
        if book_name_exist:
           Catalog.books.remove(book_name_exist[-1])
           Catalog.diff_count -=1
        else:
            print('This book is not present in the library')
    
    
    
        