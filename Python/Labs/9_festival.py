print("=" * 35)
print("   FESTIVAL DECORATION DESIGNER")
print("=" * 35)

# Take input from the user
n = int(input("Enter the number of rows: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    # Pattern 1: Star Triangle
    print("\nPattern 1: Star Triangle")
    print("-" * 30)

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    # Pattern 2: Number Triangle
    print("\nPattern 2: Number Triangle")
    print("-" * 30)

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Pattern 3: Inverted Star Triangle
    print("\nPattern 3: Inverted Star Triangle")
    print("-" * 30)

    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

    # Pattern 4: Pyramid
    print("\nPattern 4: Pyramid")
    print("-" * 30)

    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("* " * (i * 2 - 1))