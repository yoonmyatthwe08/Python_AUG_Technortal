import movie

def main():
    movie.create_table()

    while True:
        print("\n=== Movie Database System ===")
        print("1. View All Movies")
        print("2. Add New Movie")
        print("3. View Movie by ID")
        print("4. Search Movies by Director")
        print("5. Update Movie Title")
        print("6. Delete Movie")
        print("7. Add Multiple Movies")
        print("0. Exit")

        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            movie.view_all_movies()
            
        elif choice == "2":
            title = input("Enter movie title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            director = input("Enter director name: ").strip()
            if not director:
                print("Director cannot be empty.")
                continue
            year_input = input("Enter release year: ").strip()
            try:
                year = int(year_input)
            except ValueError:
                print("Invalid year. Please enter a valid number.")
                continue

        elif choice == "3":
            id_input = input("Enter movie ID: ").strip()
            try:
                movie_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            movie.view_movie_by_id(movie_id)

        elif choice == "4":
            director = input("Enter director name to search: ").strip()
            movie.search_movies_by_director(director)

        elif choice == "5":
            id_input = input("Enter movie ID to update: ").strip()
            try:
                movie_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Title cannot be empty.")
                continue
            movie.update_movie_title(movie_id, new_title)

        elif choice == "6":
            id_input = input("Enter movie ID to delete: ").strip()
            try:
                movie_id = int(id_input)
            except ValueError:
                print("Invalid ID. Please enter numbers only.")
                continue
            movie.delete_movie(movie_id)

        elif choice == "7":
            num_movies_input = input("Enter number of movies to add: ").strip()
            try:
                num_movies = int(num_movies_input)
                if num_movies <= 0:
                    print("Number of movies must be greater than zero.")
                    continue
            except ValueError:
                print("Invalid number. Please enter a positive integer.")
                continue

            movies_to_add = []
            for i in range(num_movies):
                print(f"\nEntering details for movie {i + 1}:")
                title = input("Enter movie title: ").strip()
                if not title:
                    print("Title cannot be empty. Skipping this movie.")
                    continue

                director = input("Enter director name: ").strip()
                if not director:
                    print("Director cannot be empty. Skipping this movie.")
                    continue

                year_input = input("Enter release year: ").strip()
                try:
                    year = int(year_input)
                except ValueError:
                    print("Invalid year. Skipping this movie.")
                    continue

                movies_to_add.append((title, director, year))

            if movies_to_add:
                movie.add_movie_batch(movies_to_add)
            else:
                print("No valid movies to add.")

        elif choice == "0":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose an option from 0 to 7.")

if __name__ == "__main__":
    main()