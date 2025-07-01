from controller.controller import Controller
from model.todolist import ToDOList


class ConsoleView:
    def __init__(self,  todo_list: ToDOList, controller: Controller):
        self.todo_list = todo_list

    def run(self):
        exit_run = False
        while not exit_run:
            pass



