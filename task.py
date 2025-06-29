from enums.priority import Priority


class Task:
    def __init__(self, name: str, description: str, priority):
        self.name = name
        self.description = description
        if not isinstance(priority, Priority):
            raise TypeError("Priority must be of type Priority")
        self.priority = priority

    def update_priority(self, priority):
        if not isinstance(priority, Priority):
            raise TypeError("Priority must be of type Priority")
        self.priority = priority
        return self

    def update_name(self, name):
        self.name = name
        return self

    def update_description(self, description):
        self.description = description
        return self

    def __str__(self):
        return f"Task {self.name}, priority: {self.priority}, description: {self.description}"
