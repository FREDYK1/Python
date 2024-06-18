import streamlit as sl
import mainFunctions

todos = mainFunctions.todo_list()


def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    mainFunctions.write_todos(todos)


sl.title("MY TODOLIST")
sl.subheader("Increase Your Productivity today.")
sl.write("Your todolist for today are;")


for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        mainFunctions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()


sl.text_input("", placeholder="Enter a Todo...", key="new_todo", on_change=add_todo)
