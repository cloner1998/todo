import csv

from enums.priority import Priority
from model.task import Task
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
        priority_mapping = {
            "HIGH": Priority.HIGH,
            "MEDIUM": Priority.MEDIUM,
            "LOW": Priority.LOW
        }
        with open("io/input.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                description = row["description"]
                priority_str = row["priority"]

                task_priority = priority_mapping.get(priority_str, Priority.LOW)

                task = Task(name=name, description=description, priority=task_priority)
                self.add(task)
        return self
    def save_to_output(self):
        priority_mapping = {
            Priority.HIGH : "HIGH",
            Priority.MEDIUM: "MEDIUM" ,
             Priority.LOW: "LOW"
        }
        with open("io/output.csv", "w", newline='') as file:
            fieldnames = ["name", "description", "priority"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.todos:
                writer.writerow({"name": task.name, "description": task.description,
                                 "priority": priority_mapping.get(task.priority)})

            return self
