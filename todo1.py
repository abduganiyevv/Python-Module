from utils1 import add_task, view_task, mark_done, delete_task

def main():
    tasks =[]
    while True:
        print("\nTO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("option lardan birini tanlang (1-5): ")

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("xayr! ")
            break
        else:
            print("Invalid choice. Try again.")

main()