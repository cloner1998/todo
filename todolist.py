import csv

from enums import priority
from enums.priority import Priority
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

    def update_description_of_task(self, description: str, task: Task):
        if task in self.todos:
            task.update_description(description)
        else:
            print(f"Task {task.name} not found in the list")

        return self

    def update_name_of_task(self, name: str, task: Task):
        if task in self.todos:
            task.update_name(name)
        else:
            print(f"Task {task.name} not found in the list")

        return self

    def update_priority_of_task(self, priority: Priority, task: Task):

        if task in self.todos:
            task.update_priority(priority)
        else:
            print(f"Task {task.name} not found in the list")

        return self

    def upload_from_input(self):
        with open("io/input.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                description = row["description"]
                sample_prio = row["priority"]
                if priority == Priority.HIGH:
                    sample_prio = Priority.HIGH
                elif sample_prio == Priority.MEDIUM:
                    sample_prio = Priority.MEDIUM
                elif sample_prio == Priority.LOW:
                    sample_prio = Priority.LOW

                task = Task(name=name, description=description, priority=Priority(sample_prio))
                self.add(task)
        return self
    def save_to_output(self):
        pass
