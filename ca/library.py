from datetime import datetime
from tabulate import tabulate

books = []
record_book = []  # This list records the returnings and borrowings with date and time

def load():
    with open("books.txt", "r") as file:
        for line in file:
            book = line.strip().split(',')  # Split each line by commas and remove newline
            books.append(book)

def save():
    with open("books.txt", "w") as file:
        for book in books:
            line = ','.join(book)  # Join each book's details with commas
            file.write(line + "\n")

# Add a new book function
def add(title, author, ISBN):
    books.append([title, author, ISBN, "available"])
    print("Your book is successfully added")
    head = ["Title", "Author", "ISBN", "Status"]
    print(tabulate([[title, author, ISBN, "available"]], head, tablefmt="grid"))
    save()  # Save changes immediately

# Borrow book function
def borrow(ISBN):
    for book in books:
        if book[2] == ISBN and book[3] == "available":
            print("\n\nYour book is", book[0], "by", book[1])

            today = datetime.today()
            date = today.strftime('%y / %m / %d')
            time = today.strftime('%H:%M:%S')

            print("\n\nEnter number 1 for confirm")
            print("Enter number 2 for cancel\n\n")

            confirm = input("Enter your choice  : ")
            if confirm == "1":
                book[3] = "borrowed"
                print("Book is successfully borrowed")

                borrowedbook = [[book[0], book[1], book[2], "borrowed", date, time]]
                record_book.append(borrowedbook[0])
                head = ["Title", "Author", "ISBN", "Status", "Borrowed Date", "Borrowed Time"]
                print(tabulate(borrowedbook, head, tablefmt="grid"))
                save()  # Save changes immediately
            else:
                print("Cancelled")
            return
    print("This book is not available")

# Return book function
def returned(ISBN):
    for book in books:
        if book[2] == ISBN and book[3] == "borrowed":
            print("Book is", book[0], "by", book[1])

            print("Enter 1 for confirm\nEnter 2 for cancel\n\n")
            choice = input("Enter your choice  : ")
            print()

            today = datetime.today()
            date = today.strftime('%y / %m / %d')
            time = today.strftime('%H:%M:%S')

            if choice == "1":
                print("Book is successfully returned")
                book[3] = "available"

                returnedbook = [[book[0], book[1], book[2], "returned", date, time]]
                record_book.append(returnedbook[0])
                head = ["Title", "Author", "ISBN", "Status", "Returned Date", "Returned Time"]
                print(tabulate(returnedbook, head, tablefmt="grid"))
                save()  # Save changes immediately
            else:
                print("Cancelled")
            return
    print("Entered ISBN is not correct or book is not available")

# View available books
def available():
    print("\n\nAvailable books")
    print("=" * 15)
    available_books = [book[:3] for book in books if book[3] == "available"]
    head = ["Book Title", "Author", "ISBN"]
    print(tabulate(available_books, headers=head, tablefmt="grid"))

# View borrowed books
def borrowed():
    print("\n\nBorrowed books")
    borrowed_books = [book[:3] for book in books if book[3] == "borrowed"]
    head = ["Book Title", "Author", "ISBN"]
    print(tabulate(borrowed_books, headers=head, tablefmt="grid"))

# Main function
def main():
    load()
    while True:
        print("=" * 53)
        print("Welcome to the Library Management System")
        print("=" * 53)
        print("Main Menu")
        print("-" * 9)
        print(" \nEnter 1 for adding a new book")
        print("Enter 2 for borrowing a book")
        print("Enter 3 for returning a book")
        print("Enter 4 to view available books")
        print("Enter 5 to view borrowed books")
        print("Enter 6 to view records")
        print("Enter 7 to exit\n ")
        choice = input("What's your choice  : ")
        print()

        if choice == "1":
            title = input("Enter book's title: ")
            author = input("Enter book's author: ")
            ISBN = input("Enter book's ISBN: ")
            add(title, author, ISBN)

        elif choice == "2":
            ISBN = input("Enter book's ISBN: ")
            borrow(ISBN)

        elif choice == "3":
            ISBN = input("Enter book's ISBN: ")
            returned(ISBN)

        elif choice == "4":
            available()

        elif choice == "5":
            borrowed()

        elif choice == "6":
            head = ["Title", "Author", "ISBN", "Status", "Date", "Time"]
            print(tabulate(record_book, head, tablefmt="grid"))

        elif choice == "7":
            save()
            print("Exiting the system...")
            break
        else:
            print("Invalid input")

        input("Press Enter to return to the main menu\n\n")

main()