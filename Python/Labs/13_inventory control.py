inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    print("\n" + "=" * 30)
    print("     INVENTORY CONTROL SYSTEM")
    print("=" * 30)

    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for item in inventory:
                print("-", item)

    elif choice == "2":
        item = input("Enter item name to add: ")

        if item.strip() != "":
            inventory.append(item)
            print(f"[SUCCESS] '{item}' added to inventory.")
        else:
            print("Error: Item name cannot be empty.")

    elif choice == "3":
        item = input("Enter item name to remove: ")

        if item in inventory:
            inventory.remove(item)
            print(f"[SUCCESS] '{item}' removed from inventory.")
        else:
            print(f"Error: '{item}' not found in inventory.")

    elif choice == "5":
        print("thank you for using  the inventory control system")
        break
    else:
        print("invalid choice! please enter a valid number from 1 to 5.")