class library:
    all = []
    def __init__(self, title: str, genre: str, author: str, quantity=1):
        self.book = title
        self.genre = genre
        self.author = author
        self.quantity = quantity
        
        library.all.append(self)
    
    def __repr__(self):
        return f"{self.book}', '{self.genre}', '{self.author}', {self.quantity}"
    
def user_find(): 
    user_input = input('Enter the title of the book: ')
    for i in library.all:
        if user_input == i.book:
            return f"{i} is in the catalogue"
    else:
        return "Book not found"
        
def new_book(): 
    user_input = input('Enter the title of the book: ')
    for i in library.all:
        if user_input == i.book:
            i.quantity += 1
            return f"{i} is in the catalogue, added 1 to quantity"
    else:
        user_input2 = input('Enter the genre of the book: ')
        user_input3 = input('Enter the author of the book: ')
        library(user_input, user_input2, user_input3)
        return f"{library.all[-1]} is now in the catalogue, added book to catalogue"

def remove_book():
    user_input = input("Enter the title of the book:")
    for i in library.all: 
        if user_input == i.book:
            if i.quantity > 1:
                i.quantity -= 1
                return f"{i} is in the catalogue, removed 1 from quantity"
            else:
                library.all.remove(i)
                return f"{i} is in the catalogue, removed book from catalogue"
    else:
        print('Book not found')

def display_books():
    return library.all

def user_inputs():
    while True:
        user_input = input('Enter 1 to find a book, 2 to add a book, 3 to remove a book, 4 to display all books, 5 to exit: ')
        if user_input == '1':
            print(user_find())
        elif user_input == '2':
            print(new_book())
        elif user_input == '3':
            print(remove_book())
        elif user_input == '4':
            print(display_books())
        elif user_input == '5':
            break
        else:
            return 'Invalid Input'
                
library('Harry Potter', 'Fantasy', 'J.K Rowling')
library('Lord of the Rings', 'Fantasy', 'J.R.R Tolkien')
library('The Hobbit', 'Fantasy', 'J.R.R Tolkien')
library('The Hunger Games', 'Fantasy', 'Suzanne Collins')
library('The Maze Runner', 'Fantasy', 'James Dashner')

print(library.all)
user_inputs()
