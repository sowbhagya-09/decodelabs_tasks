tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")