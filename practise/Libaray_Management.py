#LIBARAY MANGEMENT
# WE WILL HAVE TWO MAIN VARIABLES NO OF BOOKS AND THE LIST OF BOOKS

class Libaray:
    def __init__(self,name,number):
        self.name=name
        self.no_of_books=number
        self.books={}

    def addBook(self,book,author):
        self.books[book]=author

    def removebook(self,book):
        if book in self.books.keys():
            self.books.__delitem__(book)

        else:
            print("NOT FOUND")


    def showbooks(self):
        for key ,value in self.books.items():
            print(key+" ",value)



l1=Libaray("WEST",4)
l1.addBook("C++ Programming","user1")
l1.addBook("Java Programming","user2")
l1.addBook("JSS Programming","user3")
l1.addBook("Python Programming","user4")
l1.showbooks()

l1.removebook("Python Programming")
l1.showbooks()