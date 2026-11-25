import app


def read_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def main():
    app.create_tables()

    while True:
        print("\n=== School Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Enroll Student in Course")
        print("5. View Student Enrollments")
        print("6. Update Enrollment Score")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            grade = input("Enter grade/class: ").strip()
            if name and grade:
                app.add_student(name, grade)
            else:
                print("Name and grade cannot be empty.")

        elif choice == "2":
            app.view_all_students()

        elif choice == "3":
            student_id = read_int("Enter student ID to delete: ")
            app.delete_student(student_id)

        elif choice == "4":
            student_id = read_int("Enter student ID: ")
            course = input("Enter course name: ").strip()
            if not course:
                print("Course name cannot be empty.")
                continue
            score = read_float("Enter score: ")
            app.add_enrollment(student_id, course, score)

        elif choice == "5":
            student_id = read_int("Enter student ID: ")
            app.view_student_enrollments(student_id)

        elif choice == "6":
            enrollment_id = read_int("Enter enrollment ID to update: ")
            new_score = read_float("Enter new score: ")
            app.update_enrollment_score(enrollment_id, new_score)

        elif choice == "0":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose an option from 0 to 6.")


if __name__ == "__main__":
    main()