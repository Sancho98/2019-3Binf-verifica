from Book import Book


book_01 = Book("Cime tempestose ","Brontë, Emily","Rizzoli",1997,406,"IT\\ICCU\\RMS\\2313710")
book_02 = Book("{Moby Dick} 2 ","Herman Melville","Rizzoli",2009,347,"IT\\ICCU\\ANA\\0342305")

books = [book_01,book_02]
def get_books_list():
    return books