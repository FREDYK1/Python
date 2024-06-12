import mainFunctions
import FreeSimpleGUI as Gui
import time

Gui.theme("DarkBlue10")

Label = Gui.Text("Enter Your Todo:")
TextBox = Gui.InputText(tooltip="Enter Todo Here", key="todo")
add_button = Gui.Button(key="ADD", image_source="add.png", mouseover_colors="White")
EditButton = Gui.Button("Edit")
ListBox = Gui.Listbox(values=mainFunctions.todo_list(), size=(45, 10),
                      enable_events=True, key="todos")
CompleteButton = Gui.Button(key="Complete", image_source='complete.png', mouseover_colors="White")
ExitButton = Gui.Button("Exit", button_color="Red")
ClockTime = Gui.Text("", key="Clock")

window = Gui.Window("My Todos App", layout=[[ClockTime],
                                            [Label, TextBox, add_button],
                                            [ListBox, EditButton, CompleteButton],
                                            [ExitButton]],
                    font=("Arial", 10))


while True:
    event, value = window.read(timeout=1000)
    window["Clock"].update(values=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "ADD":
            todos = mainFunctions.todo_list()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            mainFunctions.write_todos(todos)
            window['todos'].update(todos)
        case "Edit":
            try:
                todo_to_edit = value["todos"][0]
                new_todo = value["todo"]
                todos = mainFunctions.todo_list()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                mainFunctions.write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                Gui.popup("Select a todo to edit.", font=("Helvetica", 15))
        case "Complete":
            try:
                TodoToComplete = value["todos"][0]
                todos = mainFunctions.todo_list()
                todos.remove(TodoToComplete)
                mainFunctions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value='')
            except IndexError:
                Gui.popup("Select a completed todo", font=("Helvetica", 15))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=value['todos'][0])

        case Gui.WINDOW_CLOSED:
            break
