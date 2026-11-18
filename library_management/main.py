import app

def main():
    app.create_table()

    while True:
        print("\n=== Library Management System ===")
        print("1. View All Books")
        print("2. Add New Book")
        print("3. View Book by ID")
        print("4. Search Books by Author")
        print("5. Update Book Title")
        print("6. Delete Book")
        print("7. Add Multiple Books")
        print("0. Exit")

        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            app.view_all_books()

        elif choice == "2":
            title = input("Enter book title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            author = input("Enter author name: ").strip()
            if not author:
                print("Author cannot be empty.")
                continue
            app.add_book(title, author)

        elif choice == "3":
            id_input = input("Enter book ID: ").strip()
            try:
                book_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            app.view_books_by_id(book_id)

        elif choice == "4":
            author = input("Enter author name to search: ").strip()
            app.search_books_by_author(author)

        elif choice == "5":
            id_input = input("Enter book ID to update: ").strip()
            try:
                book_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue

            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Title cannot be empty.")
                continue
            app.update_book_title(book_id, new_title)

        elif choice == "6":
            id_input = input("Enter book ID to delete: ").strip()
            try:
                book_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            app.delete_book(book_id)

        elif choice == "7":
            num_books_input = input("Enter number of books to add: ").strip()
            try:
                num_books = int(num_books_input)
                if num_books <= 0:
                    print("Number of books must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid number. Please enter a positive integer.")
                continue

            books_to_add = []
            for i in range(num_books):
                print(f"\nEntering details for book {i + 1}:")
                title = input("Enter book title: ").strip()
                if not title:
                    print("Title cannot be empty. Skipping this book.")
                    continue

                author = input("Enter author name: ").strip()
                if not author:
                    print("Author cannot be empty. Skipping this book.")
                    continue

                books_to_add.append((title, author))

            if books_to_add:
                app.add_book_batch(books_to_add)
            else:
                print("No valid books to add.")

        elif choice == "0":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose an option from 0 to 6.")

if __name__ == "__main__":
    main()