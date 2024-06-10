import mainFunctions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Enter, Print, Exit , Complete or Edit Todos : ")
    user_input = user_input.strip()
    user_input = user_input.capitalize()

    if user_input.startswith("Enter"):
        user_input = user_input[6:] + "\n"
        user_input = user_input.title()

        todos = mainFunctions.todo_list()

        todos.append(user_input)

        mainFunctions.write_todos(todos)

    elif user_input.startswith("Print"):

        todos = mainFunctions.todo_list()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index + 1}. {todo}")

    elif user_input.startswith("Edit"):
        try:
            number = int(user_input[5:])
            number = number-1

            todos = mainFunctions.todo_list()

            new_todo = input("What is your new todo :")
            todos[number] = new_todo.capitalize() + '\n'

            mainFunctions.write_todos(todos)

        except ValueError:
            print("Your Instruction is not valid. ")
        continue

    elif user_input.startswith("Complete"):
        try:
            number_completed = int(user_input[9:])

            todos = mainFunctions.todo_list()

            removed_todo = todos[number_completed - 1]

            todos.pop(number_completed - 1)

            mainFunctions.write_todos(todos)

            Message = f"{removed_todo.strip('\n')} has been removed."
            print(Message)
        except ValueError:
            print("Your Instruction is not valid. ")
        continue

    elif user_input.startswith("Exit"):
        break
    else:
        print("The Command isn't Valid. ")


print("\n" + "BYE!, See You Soon.")
