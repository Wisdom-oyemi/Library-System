class Library():
    def __init__(self, name):
        self.name = name
        self.rating = 0
    
    class Book():
        def __init__(self, title, author, year, library):
            self.library = library
            self.title = title
            self.author = author
            self.year = year

        def showName(self):
            print(self.title)
        
        def showAuthor(self):
            print(self.author)
        
        def showYear(mine):
            print(mine.year)
        
        def showRating(self):
            print (self.library.rating)

'''
class LibraryPatron():
        def __init__(self, name, age):
            self.name = name
            self.age = age
'''
if __name__ == "__main__":
    libraryObject = Library("The WizCs")

    book1 = libraryObject.Book("The Life of a Wizkid", "Wisdom Oyemi", 2027, libraryObject)
    book2 = libraryObject.Book("My Home: 'The Rainbow Drew'", "Jovan Clue", 2025, libraryObject)


    book1.showName()
    book1.showRating()