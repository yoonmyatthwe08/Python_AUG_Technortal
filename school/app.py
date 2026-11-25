import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "school.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_tables():
    conn = get_connection()
    try:
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT NOT NULL
            )
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course TEXT NOT NULL,
                score REAL NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE
            )
            """)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def add_student(name, grade):
    conn = get_connection()
    try:
        with conn:
            cur = conn.execute(
                "INSERT INTO students (name, grade) VALUES (?, ?)",
                (name, grade),
            )
        print(f"Student '{name}' added with ID {cur.lastrowid}.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def view_all_students():
    conn = get_connection()
    try:
        cur = conn.execute("SELECT id, name, grade FROM students ORDER BY id")
        rows = cur.fetchall()
        if not rows:
            print("No students found.")
            return
        print("\n--- Students ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Grade: {row[2]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def delete_student(student_id):
    conn = get_connection()
    try:
        with conn:
            cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
            if cur.rowcount == 0:
                print(f"No student found with ID {student_id}.")
            else:
                print(f"Student ID {student_id} and their enrollments deleted.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def add_enrollment(student_id, course, score):
    conn = get_connection()
    try:
        with conn:
            conn.execute(
                "INSERT INTO enrollments (student_id, course, score) VALUES (?, ?, ?)",
                (student_id, course, score),
            )
        print(f"Enrolled student ID {student_id} in '{course}' (Score: {score}).")
    except sqlite3.IntegrityError:
        print(f"Student ID {student_id} does not exist. Add the student first.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def view_student_enrollments(student_id):
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            SELECT e.id, s.name, e.course, e.score
            FROM enrollments e
            JOIN students s ON e.student_id = s.id
            WHERE e.student_id = ?
            ORDER BY e.id
            """,
            (student_id,),
        )
        rows = cur.fetchall()
        if not rows:
            print(f"No enrollments found for student ID {student_id}.")
            return
        print(f"\n--- Enrollments for {rows[0][1]} (ID: {student_id}) ---")
        for row in rows:
            print(f"Enrollment ID: {row[0]} | Course: {row[2]} | Score: {row[3]}")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()


def update_enrollment_score(enrollment_id, new_score):
    conn = get_connection()
    try:
        with conn:
            cur = conn.execute(
                "UPDATE enrollments SET score = ? WHERE id = ?",
                (new_score, enrollment_id),
            )
            if cur.rowcount == 0:
                print(f"No enrollment found with ID {enrollment_id}.")
            else:
                print(f"Enrollment ID {enrollment_id} score updated to {new_score}.")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()