# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:02:59 2020

@author: Ratnambar Gupta
"""

from Catalog import Catalog
class BookIssue:
    def issueBook(book,librarian_id,librarian_name,issueDay):
        catalog = Catalog()
        catalog.setLibrarianForBookItem(book, librarian_id, librarian_name, issueDay)
        
    def returnBook(book, librarian_id):
        catalog = Catalog()
        catalog.retunBookUpdateCatalog(book, librarian_id)
        

