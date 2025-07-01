from enums.priority import Priority
from model.task import Task
from model.todolist import ToDOList


class Controller:
    def __init__(self, todo_list: ToDOList):
        self.todo_list = todo_list

    def add_task(self, task: Task):
        self.todo_list.add(task)
        return self.todo_list

    def remove_task(self, task: Task):
        self.todo_list.remove(task)
        return self.todo_list

    def get_all_tasks(self):
        return self.todo_list.show_all_tasks()

    def update_name_task(self, task: Task, name: str):
        self.todo_list.update_name_of_task(name, task)
        return self.todo_list

    def update_description_task(self, task: Task, description: str):
        self.todo_list.update_description_of_task(description, task)
        return self.todo_list

    def update_priority_task(self, task: Task, priority: str):
        priority_mapping = {
            "HIGH": Priority.HIGH,
            "MEDIUM": Priority.MEDIUM,
            "LOW": Priority.LOW
        }
        self.todo_list.update_priority_of_task(priority_mapping.get(priority), task)
        return self.todo_list

    def upload_date(self):
        self.todo_list.upload_from_input()
        return self.todo_list

    def save_data(self):
        self.todo_list.save_to_output()
        return self.todo_list
