from task import Task
from typing import List


class ToDOList:

    def __init__(self, tasks: List[Task]) -> None:
        self.todos = tasks

    def add(self, task: Task):
        self.todos.append(task)
        return self

    def remove(self, task: Task):
        try:
            self.todos.remove(task)
        except ValueError:
            print(f"Task {task.name} not found in the list")
        return self

    def show_all_tasks(self):
        for task in self.todos:
            print(task)

    def save_csv(self):
        pass
