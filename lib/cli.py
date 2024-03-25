from myfunction import (
    list_users,
    get_user_by_id,
    get_user_by_name,
    create_new_user,
    delete_user_command,
    list_tasks,
    get_task_command,
    update_task_command,
    create_task_command,
    delete_task_command,
    list_categories,
    get_category_command,
    update_category_command,
    create_category_command,
    delete_category_command,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_users()
            input("Press ENTER to Continue")
        elif choice == "2":
            get_user_by_id()
            input("Press ENTER to Continue")
        elif choice == "3":
            get_user_by_name()
            input("Press ENTER to Continue")
        elif choice == "4":
            create_new_user()
            input("Press ENTER to Continue")
        elif choice == "5":
            delete_user_command()
            input("Press ENTER to Continue")
        elif choice == "6":
            list_tasks()
            input("Press ENTER to Continue")
        elif choice == "7":
            get_task_command()
            input("Press ENTER to Continue")
        elif choice == "8":
            update_task_command()
            input("Press ENTER to Continue")
        elif choice == "9":
            create_task_command()
            input("Press ENTER to Continue")
        elif choice == "10":
            delete_task_command()
            input("Press ENTER to Continue")
        elif choice == "11":
            list_categories()
            input("Press ENTER to Continue")
        elif choice == "12":
            get_category_command()
            input("Press ENTER to Continue")
        elif choice == "13":
            update_category_command()
            input("Press ENTER to Continue")
        elif choice == "14":
            create_category_command()
            input("Press ENTER to Continue")
        elif choice == "15":
            delete_category_command()
            input("Press ENTER to Continue")
        elif choice == "16":
            break
        else:
            print("Invalid choice")


def menu():
    print("1. List all users")
    print("2. Get user by ID")
    print("3. Get user by Name")
    print("4. Create new user")
    print("5. Delete user")
    print("6. List all tasks")
    print("7. Get task by ID")
    print("8. Update task")
    print("9. Create new task")
    print("10. Delete task")
    print("11. List all categories")
    print("12. Get category by ID")
    print("13. Update category")
    print("14. Create new category")
    print("15. Delete category")
    print("16. Exit")
    print("Please select an option:")


if __name__ == "__main__":
    main()
