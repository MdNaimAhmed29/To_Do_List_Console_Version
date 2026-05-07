while True:
    user_action = input("Add, Show, Edit, Complete, Exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            todo = input("Enter your Todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"{index + 1}- {item.strip()}")  # clean output

        case "edit":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(input("Enter the number of the todo to edit: "))
            number -= 1

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":

            number = int(input("Enter the number of the todo to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' removed from the list."
            print(message)

        case "exit":
            break