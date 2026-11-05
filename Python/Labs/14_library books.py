# Library Book Collection

# Initial book records
books = [
    {
        "title": "Python Programming",
        "author": "John Smith",
        "year": 2022,
        "category": "Programming"
    },
    {
        "title": "Data Science Basics",
        "author": "Alice Brown",
        "year": 2023,
        "category": "Data Science"
    },
    {
        "title": "Cloud Computing",
        "author": "David Lee",
        "year": 2021,
        "category": "Cloud Computing"
    },
    {
        "title": "Cybersecurity Essentials",
        "author": "Mark Wilson",
        "year": 2024,
        "category": "Cybersecurity"
    }
]

# Student wishlist
student_wishlist = set()

# Display menu
def display_menu():
    print("\nSelect an operation:")
    print("1. View Catalogued Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")


# Option 1: View books
def view_books():
    print("\n=== CATALOGUED BOOKS ===")

    if not books:
        print("No books available.")
        return

    for i, book in enumerate(books, start=1):
        print(f"\nBook {i}")
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Category:", book["category"])

    print("\nTotal books:", len(books))


# Option 2: Add a new book
def add_book():
    print("\n=== ADD NEW BOOK ===")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return

    category = input("Enter book category: ").strip()

    if not title or not author or not category:
        print("All fields are required.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "category": category
    }

    books.append(book)
    print(f'Success! "{title}" added to the library.')


# Option 3: View unique categories
def view_categories():
    categories = {book["category"] for book in books}

    print("\n=== UNIQUE LIBRARY CATEGORIES ===")

    for category in sorted(categories):
        print("-", category)

    print("Total unique categories:", len(categories))


# Option 4: Add category to wishlist
def add_to_wishlist():
    print("\n=== ADD TO STUDENT WISHLIST ===")

    category = input("Enter requested category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    student_wishlist.add(category)
    print(f'Success! "{category}" added to student wishlist.')


# Option 5: Category gap analysis
def category_gap_analysis():
    library_categories = {
        book["category"] for book in books
    }

    print("\n" + "=" * 15 + " CATEGORY GAP ANALYSIS " + "=" * 15)

    print("\nLibrary Holdings (Set):")
    print(library_categories)

    print("\nStudent Wishlist (Set):")
    print(student_wishlist)

    # Categories available in both
    intersection = library_categories & student_wishlist

    # Categories students want but library lacks
    difference = student_wishlist - library_categories

    # All categories combined
    union = library_categories | student_wishlist

    print("\n1. Already in Stock (Intersection):")
    print(intersection if intersection else "None")

    print("\n2. Purchase Order Needed (Difference):")
    print(difference if difference else "None")

    print("\n3. Full Combined Genre Coverage (Union):")
    print(union)

    print("\n" + "=" * 50)


# Main program loop
while True:
    display_menu()

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        view_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        view_categories()

    elif choice == "4":
        add_to_wishlist()

    elif choice == "5":
        category_gap_analysis()

    elif choice == "6":
        print("Thank you for using Library Book Collection!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")