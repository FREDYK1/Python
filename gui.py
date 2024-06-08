import mainFunctions
import FreeSimpleGUI as Gui

Label = Gui.Text("Enter Your Todo:")
TextBox = Gui.InputText(tooltip="Enter Todo Here", key="todo")
add_button = Gui.Button("ADD")
EditButton = Gui.Button("Edit")
ListBox = Gui.Listbox(values=mainFunctions.todo_list(), size=(45, 10),
                      enable_events=True, key="todos")

window = Gui.Window("My Todos App", layout=[[Label, TextBox, add_button], [ListBox, EditButton]],
                    font=("Arial", 10))



while True:
    event, value = window.read()
    match event:
        case "ADD":
            todos = mainFunctions.todo_list()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            mainFunctions.write_todos(todos)
            window['todos'].update(todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"]
            todos = mainFunctions.todo_list()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            mainFunctions.write_todos(todos)
            window['todos'].update(todos)
        case "todos":
            window["todo"].update(value=value['todos'][0])

        case Gui.WINDOW_CLOSED:
            break
