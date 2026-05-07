while True:
    user_action = input("Add, Show, Edit, Complete, Exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif 'edit' in user_action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        number = int(user_action[5:])
        number -= 1

        new_todo = input("Enter new todo: ") + "\n"
        todos[number] = new_todo

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:

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

    elif 'exit' in user_action:
        break

    else:
        print("Invalid command. Please try again.")

print("Goodbye!")