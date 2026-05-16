import json
import streamlit as st

st.title("TO DO APP")
st.subheader("Simple Streamlit To-Do App")

# ---------- Load Data ----------
def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# ---------- Save Data ----------
def save_todos():
    with open("todos.json", "w") as file:
        json.dump(st.session_state.todos, file)

# ---------- Initialize ----------
if "todos" not in st.session_state:
    st.session_state.todos = load_todos()

# ---------- Add Todo ----------
def add_todo():
    new_todo = st.session_state.new_todo.strip()
    if new_todo:
        st.session_state.todos.append({
            "task": new_todo,
            "completed": False
        })
        st.session_state.new_todo = ""
        save_todos()

st.text_input("Add a new task:", key="new_todo", on_change=add_todo)

# ---------- Display ----------
if st.session_state.todos:
    for index, todo in enumerate(st.session_state.todos):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            completed = st.checkbox("", value=todo["completed"], key=f"checkbox_{index}")
            st.session_state.todos[index]["completed"] = completed
            save_todos()
        with col2:
            st.write(todo["task"])
else:
    st.write("No tasks yet! Add a task to get started.")

def delete_completed():
    st.session_state.todos = [todo for todo in st.session_state.todos if not todo["completed"]]
    save_todos()
st.button("Delete Completed Tasks", on_click=delete_completed)
