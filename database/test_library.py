from Library  import Library
from Book import Book




marconi = Library("BIBLIOTECA IIS Marconi","CIVMA")
harry_potter = book("Harry Potter, spiderman e broccoli","J.K.Rowling","Salani Editore",1998,1111,6464646464)

assert marconi.name == "BIBLIOTECA IIS Marconi"
assert marconi.sbn_code == "6464646464"
assert marconi.last_update == ""
assert  len(marconi.catalogue) == 0

marconi.add_book(harry_potter)

assert len(marconi.catalogue) == "1"