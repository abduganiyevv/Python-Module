
def add_task(tasks):
    task = input("task ni kiriting: ")
    task.append({"task": task, "done": False})

def view_task(tasks):
    if not tasks:
        print("task hali ham yoq. ")
        return
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i + 1}. {status} {t['task']}")

def mark_done(tasks):
    view_task(tasks)  
    try: 
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks): 
            tasks[index]["done"] = True
            print("taskingiz qohsildi")
        else:
            print("bunaqa task yoq")
    except ValueError:
        print("iltimos raqam kiriting")

def delete_task(tasks):
    view_task(tasks)
    try:
        index = int(input("ochirmoqchi bolgan taskni kiritng: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"task ochirildi: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Iltimos raqamni kiritng.")