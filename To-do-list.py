# My simple to-do list

tasks = []

while True:
    print("\n==== MY TO-DO LIST ====")
    print("1. View Tasks") 
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nMy Tasks:")
            count = 1
            for task in tasks:
                print(count, "-", task["name"], "| Deadline:", task["deadline"])
                count += 1

    elif choice == "2":
        task_name = input("Enter task name: ")
        due_date = input("Enter deadline (DD/MM/YYYY): ")

        task = {
            "name": task_name,
            "deadline": due_date
        }

        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to remove.")
        else:
            print("\nTasks:")
            count = 1
            for task in tasks:
                print(count, "-", task["name"])
                count += 1

            number = int(input("Which task do you want to remove? "))

            if number >= 1 and number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print("Removed:", deleted["name"])
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Please enter 1, 2, 3 or 4.")


        