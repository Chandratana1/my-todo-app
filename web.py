from tabnanny import check

import streamlit as st
import web_functions

todos = web_functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    web_functions.write_todos(todos)





st.title("My Todo App")
st.subheader("This is my sub header todo app")
st.write("This is wonderful")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        web_functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "Enter a todo, I am label:", placeholder = "Add a new todo, I am Placeholder",
              on_change=add_todo, key = 'new_todo')


st.session_state