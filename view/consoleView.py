from controller.controller import Controller
from enums.priority import Priority
from model.task import Task
from model.todolist import ToDOList


def make_default_todo_list(self):
    task = Task("name", "description", Priority.MEDIUM)
    list_todo = [task]
    todo_list = ToDOList(list_todo)
    return todo_list


def upload_todo_list(self):
    return self.controller.upload_data()


def check_permission(self, permission: str):
    if permission.upper() == "Y":
        return True
    if permission.upper() == "N":
        return False
    return "your input is not valid"


def modify_todo_list(todo_list, modification_ans):
    pass


def save_todo_list(todo_list, save_ans):
    pass


class ConsoleView:
    def __init__(self, controller: Controller):
        self.controller = controller

    def run(self):
        todo_list = make_default_todo_list(self)
        ans = input("do you want to upload your todolist (from io/input.csv)? (y/n)")
        if check_permission(self, ans):
            todo_list = upload_todo_list(self)

        exit_run = False
        while not exit_run:
            modification_ans = input("how do you want to modify your todo list? (add, remove, show")
            modify_todo_list(todo_list, modification_ans)

            exit_ans = input("Do you want to exit? (y/n)")
            if check_permission(self, exit_ans):
                exit_run = True

            pass

        save_ans = input("Do you want to save your todolist? (y/n)")
        save_todo_list(todo_list, save_ans)
