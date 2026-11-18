import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "library.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL)
            """)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def add_book(title, author):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute(
                "INSERT INTO books (title, author) VALUES (?, ?)", (title, author)
            )
        print(f"Book '{title}' added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def add_book_batch(books):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books)
        print(f"{len(books)} books added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def view_all_books():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute("SELECT id, title, author FROM books")
        rows = cur.fetchall()

        if not rows:
            print("No books found.")
            return
        print("\n--- Book List ---")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def view_books_by_id(book_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, title, author FROM books WHERE id = ?", (book_id,)
        )
        row = cur.fetchone()
        if not row:
            print(f"No book found with ID {book_id}.")
            return
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def search_books_by_author(author):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, title, author FROM books WHERE author = ?", (author,)
        )
        rows = cur.fetchall()
        if not rows:
            print(f"No books found by author '{author}'.")
            return
        print(f"\n--- Books by Author: {author} ---")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def update_book_title(book_id, new_title):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute(
                "UPDATE books SET title = ? WHERE id = ?", (new_title, book_id)
            )
            if cur.rowcount == 0:
                print(f"No book found with ID {book_id}.")
            else:
                print(f"Book ID {book_id} title updated to '{new_title}'.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def delete_book(book_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
            if cur.rowcount == 0:
                print(f"No book found with ID {book_id}.")
            else:
                print(f"Book ID {book_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


