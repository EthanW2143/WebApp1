FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """ Grabs list of todos from todos.txt
    and returns it as a list """
    with open(file_path, 'r') as todo_file:
        ret_todos = todo_file.readlines()
    return ret_todos


def write_todos(todos, file_path=FILEPATH):
    """ Accepts a list of todos as a parameter, and writes
    it to a file """
    with open(file_path, 'w') as todo_file:
        for todo in todos:
            todo_file.write(todo.strip() + "\n")

