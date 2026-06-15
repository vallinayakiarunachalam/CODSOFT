tasks = []
while True:
    print("\n==== TO-DO LIST ====")
    print("1. View Tasks")
    print("2. Add Tasak")
    print("3. Mark Task as Finished")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        if len(tasks) == 0:
            print("No Tasks Available.")
        else:
            print("\n Your Tasks:")
            for i in range(len(tasks)):
                status = "*" if tasks[i] ["done"] else "x"
                print(f"{i + 1}.{tasks[i] ['tasks']} [{status}]")
    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append({"task":task_name, "done": False})
        print("Task added successfully!")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}.{tasks[i] ['task']}")
            num = int(input("Enter task number to mark Finished: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1] ["done"] = True
                print("Task marked as Finished!")
            else:
                print("Invalid task number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}.{tasks[i]['task']}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print(f"Deleted task: {deleted['task']}")
            else:
                print("Invalid task number.")
    elif choice == "5":
        print("Thank You for using To-Do List!")
        break
    else:
        print("Invalid choice.Please try again.")
                        
               







