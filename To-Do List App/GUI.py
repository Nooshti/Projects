import functions
import FreeSimpleGUI as fs
import time

fs.theme("DarkPurple4") # colour theme available on simple gui website

clock = fs.Text('', key='clock')
label = fs.Text("Type in a to-do")
input_box = fs.InputText(tooltip="Enter todo:", key="todo")
add_button = fs.Button("Add", size=10)
list_box = fs.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10]) # gets the todo list using functions
edit_button = fs.Button("Edit")
# layout expects a list
# if u want to put input_box below label then put both in separate brackets

complete_button = fs.Button("Complete")
exit_button = fs.Button("Exit")

window = fs.Window('My To-Do App',
                   layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read(timeout=200) # method which returns something + timeout runs the program every 200 milliseconds
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"    # values['todo'] gives the value of the key 'todo'
            todos.append(new_todo)  # adds the new todo
            functions.write_todos(todos)    # overwrites the old todo list with new one

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]   # gets only the string from the event (old todo)
                new_todo = values['todo'] + "\n"  # new todo which replaces old one (user clicks on old one)

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)    # overwrites old todo list
                window['todos'].update(values=todos)
            except IndexError:
                fs.popup("Please select an item first.", font=("Helvetica", 10))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fs.popup("Please select an item first.", font=("Helvetica", 10))

        case "Exit":
            break

        case  'todos':
            window['todo'].update(value=values['todos'][0])    # todo item in gui which we have clicked, appears in input box
        case fs.WIN_CLOSED:
            break

window.close()