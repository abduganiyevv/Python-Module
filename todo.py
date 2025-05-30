from utils import add_task,view_tasks,mark_done,delete_task

def main():
    tasks = []
    while True:
        print("\n📋 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye! All tasks lost (not saved).")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
