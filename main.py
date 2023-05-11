def get_todos(filepath="todos.txt"):
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Add or Show, edit, complete or exit? ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.title() + '\n')

        write_todos(todos,"todos.txt")

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos,"todos.txt")

        except ValueError:
            print("Your Command Is Not Valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos,"todos.txt")

            message = "\n" + f"'{todo_to_remove}' was removed" + "\n"
            print(message)
        except ValueError and IndexError:
            print("Your Command Is Not Valid.")
            continue

    elif 'exit' in user_action:
        break

    else:
        print(" Command is not valid!!! \n Please Enter again")
print("Okay!")
