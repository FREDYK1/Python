import streamlit
import streamlit as sl
import mainFunctions


sl.title("MY TODOLIST")
sl.subheader("Increase Your Productivity today.")
sl.write("Your todolist for today are;")

todos = mainFunctions.todo_list()

for todo in todos:
    sl.checkbox(todo)

sl.text_input("", placeholder="Enter a Todo...")