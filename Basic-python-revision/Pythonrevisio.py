import json
import streamlit as st

st.title("TO DO APP")
st.subheader("Simple Streamlit To-Do App")
st.markdown("""
    <style>
    div[data-testid="stCheckbox"] {
        margin-top: 14px;
    }
    </style>
""", unsafe_allow_html=True)


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
def display_todos():
    if st.session_state.todos:

        for index, todo in enumerate(st.session_state.todos):

            col1, col2, col3, col4 = st.columns([0.1,0.6,0.1,0.2])

            # Checkbox
            with col1:
                completed = st.checkbox(
                    "",
                    value=todo["completed"],
                    key=f"checkbox_{index}"
                )
                if completed != todo["completed"]:
                    st.session_state.todos[index]["completed"] = completed
                    save_todos()

            # Task Text
            with col2:
                if st.session_state.get(f"editing_{index}", False):

                    edited_task = st.text_input(
                        "Edit Task",
                        value=todo["task"],
                        key=f"edit_input_{index}"
                    )

                    if st.button("Save", key=f"save_{index}"):
                        st.session_state.todos[index]["task"] = edited_task
                        st.session_state[f"editing_{index}"] = False
                        save_todos()
                        st.rerun()

                else:
                    st.write(todo["task"])

            # Edit Button
            with col3:
                if st.button("Edit", key=f"edit_{index}"):
                    st.session_state[f"editing_{index}"] = True

            # Delete Button
            with col4:
                if st.button("Delete", key=f"delete_{index}"):
                    del st.session_state.todos[index]
                    save_todos()
                    st.rerun()

display_todos()

