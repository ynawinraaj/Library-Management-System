class Library:
    def __init__(self,list,name):
        self.list=list
        self.name=name
        self.lenDict={}
    def displayBooks(self):
        print("we have the following books in the library:{self.name}")
        for book in list:
            print(book)
    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print("Lender-Book database has been updated. You can take the book now.")
    def addBook(self, book):
            self.booksList.append(book)
            print(f"{book} has been added to the book list.")
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("That book wasn't borrowed from us.")
        
if __name__ == '__main__':
        books = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics','Algorithms by CLRS'], "Let's Upskill")
user_name = input("Welcome to our library! Please enter your name: ")
while True:
        print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
        user_choice = input("Enter your choice to continue: ")
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a valid option.")
            continue
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend: ")
            books.lendBook(user_name, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        elif user_choice == '5':
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break