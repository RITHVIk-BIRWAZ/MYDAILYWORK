# To-Do List Application

tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted = tasks.pop(task_num - 1)
                print(f"Deleted task: {deleted}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
