while True:
    user_action = input("Add, Show, Edit, Complete, Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):

        try:

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            number = int(user_action[5:])
            number -= 1

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    elif user_action.startswith('complete'):

        try:

            number = int(user_action[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' removed from the list."
            print(message)

        except IndexError:
            print("Invalid index. Please try again.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command. Please try again.")

print("Goodbye!")