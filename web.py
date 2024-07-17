import streamlit as st
import todos_def


todos = todos_def.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    todos_def.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("ToDo List")
st.subheader("Enter a ToDo:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        todos_def.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="",
              placeholder="Add new todo...",
              on_change=add_todo,
              key='new_todo')
