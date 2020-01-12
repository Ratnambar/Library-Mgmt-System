# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian


b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')




b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')


catalog.displayAllBooks()

catalog.searchByName('Lean In')
catalog.searchByAuthor('J.K.Rowling')

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
m2 = Member("Chaitali","Pune",28,'chaitali123','HS1166')
m3 = Member("Jane","Punr",25,'jane123','HS1177')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (m1)
print (librarian)

#m1.issueBook


librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 

lib1 = librarian.addBook('Lean In','Sheryl Sandberg', 2018, 600)
catalog.addBookItem(lib1,'454hs','H1B6')
catalog.addBookItem(lib1,'456hs','H1B7')

lib2 = librarian.addBook('Harry Potter','J.K.Rowling', 2013, 600)
catalog.addBookItem(lib2,'545hs','H2B1')
catalog.addBookItem(lib2,'656hs','H2B2')
librarian.removeBook('Harry Potter')

Catalog.books = []
Catalog.diff_count = 0

m1.issueBook('Lean In')
m2.issueBook('Lean In')

m1.returnBook('Lean In')


catalog.displayLibrarianDetails()




