import mainFunctions
import FreeSimpleGUI

Label = FreeSimpleGUI.Text("Enter Your Todo:")
TextBox = FreeSimpleGUI.InputText(tooltip="Enter Todo Here", key="todo")
add_button = FreeSimpleGUI.Button("ADD")
window = FreeSimpleGUI.Window("My Todos App", layout=[[Label, TextBox, add_button]], font=("Arial", 10))

while True:
    event, value = window.read()
    match event:
        case "ADD":
            todos = mainFunctions.todo_list()
            new_todo = value["todo"]
            todos.append(new_todo)
            mainFunctions.write_todos(todos)
        case FreeSimpleGUI.WINDOW_CLOSED:
            break
