from library import Library

if __name__ == "__main__":

    my_library = Library()
    is_running = True
    while is_running:
        print("Wellcome to The Lion Library!\nChoose from the menu:")
        print(" 1.add book\n 2.add user\n 3.borrow book\n 4.return book\n 5.get available books\n 6.search book\n 7.for exit")
        action = int(input("Enter here -> "))

        if action == 1: # add_book
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book isbn: ")
            Library.add_book(title, author, isbn)

        if action == 2: # add_user
            name = input("Enter user name: ")
            id = input("Enter user id: ")
            Library.add_user(name, id)

        if action == 3: # borrow_book
            book = input("Enter book: ")
            user = input("Enter user: ")
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            Library.borrow_book(book, user, user_id, book_isbn)

        if action == 4: # return_book
            book = input("Enter book: ")
            user = input("Enter user: ")
            user_id = input("Enter user id: ")
            book_isbn = input("Enter book isbn: ")
            Library.return_book(book, user, user_id, book_isbn)

        if action == 5: # list_available_books
            Library.list_available_books(my_library)

        if action == 6: # search_book
            key = input("Enter book title/auther/isbn: ")
            Library.search_book(my_library, key)

        if action == 7: # exit
            print("Goodbye!")
            is_running = False

