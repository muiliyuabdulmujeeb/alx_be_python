def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
            print("Item added to the list")
        elif choice == '2':
            item_to_remove = input("Enter the item you want to remove: ")
            if item_to_remove not in shopping_list:
                print("The item you input is not in the list, Please input a valid item")
            shopping_list.remove(item_to_remove)
            print("Item removed")
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()