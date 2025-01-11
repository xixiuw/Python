
#### 2.2 Simple To-Do List

def todo_list():
    tasks = []
    
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == "2":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == "3":
            if tasks:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
        elif choice == "4":
            break

