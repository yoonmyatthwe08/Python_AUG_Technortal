import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "movies.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director TEXT NOT NULL,
                year INTEGER NOT NULL)
            """)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def add_movie(title, director, year):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute(
                "INSERT INTO movies (title, director, year) VALUES (?, ?, ?)", 
                (title, director, year)
            )
        print(f"Movie '{title}' added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def add_movie_batch(movies):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.executemany(
                "INSERT INTO movies (title, director, year) VALUES (?, ?, ?)", 
                movies
            )
        print(f"{len(movies)} movies added successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def view_all_movies():
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute("SELECT id, title, director, year FROM movies")
        rows = cur.fetchall()
        if not rows:
            print("No movies found.")
            return
        print("\n--- Movie List ---")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Director: {row[2]}, Year: {row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def view_movie_by_id(movie_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, title, director, year FROM movies WHERE id = ?", (movie_id,)
        )
        row = cur.fetchone()
        if not row:
            print(f"No movie found with ID {movie_id}.")
            return
        print(f"ID: {row[0]}, Title: {row[1]}, Director: {row[2]}, Year: {row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def search_movies_by_director(director):
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, title, director, year FROM movies WHERE director = ?", (director,)
        )
        rows = cur.fetchall()
        if not rows:
            print(f"No movies found by director '{director}'.")
            return
        print(f"\n--- Movies by Director: {director} ---")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Director: {row[2]}, Year: {row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def update_movie_title(movie_id, new_title):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute(
                "UPDATE movies SET title = ? WHERE id = ?", (new_title, movie_id)
            )
            if cur.rowcount == 0:
                print(f"No movie found with ID {movie_id}.")
            else:
                print(f"Movie ID {movie_id} title updated to '{new_title}'.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def delete_movie(movie_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            cur = conn.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            if cur.rowcount == 0:
                print(f"No movie found with ID {movie_id}.")
            else:
                print(f"Movie ID {movie_id} deleted successfully.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


