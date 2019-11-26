from datetime import datetime
from Book import Book


class Library:
    def __init__(self,name,sbn_code):
        self.name = name
        self.sbn_code = sbn_code
        self.last_update = datetime.now()
        self.catalogue = []

    def add_book(self,book):
        self.catalogue.append(book)

marconi = Library("BIBLIOTECA IIS Marconi","CIVMA")
harry_potter = Book("Cime tempestose ","Brontë, Emily","Rizzoli",1997,1111,"IT\ICCU\RMS\2313710")

assert marconi.name == "BIBLIOTECA IIS Marconi"
assert marconi.sbn_code == "IT\ICCU\RMS\2313710"
assert marconi.last_update == ""
assert  len(marconi.catalogue) == 0

marconi.add_book(harry_potter)

assert len(marconi.catalogue) == 




