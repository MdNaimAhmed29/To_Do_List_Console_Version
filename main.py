#from functions import get_todos, write_todos
import functions

import time

now = time.strftime("%Y-%m-%d %H:%M:%S")

print(f"Welcome to the To-Do List App! Current time: {now}")

while True:
    user_action = input("Add, Show, Edit, Complete, Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):

        try:

            todos = functions.get_todos()

            number = int(user_action[5:])
            number -= 1

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    elif user_action.startswith('complete'):

        try:

            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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