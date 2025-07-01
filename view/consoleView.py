from enums.priority import Priority
from model import todolist
from model.task import Task
from model.todolist import ToDOList


def make_default_todo_list():
    task = Task("default", "default", Priority.MEDIUM)
    list_todo = [task]
    todo_list = ToDOList(list_todo)
    return todo_list


def check_permission(permission: str):
    if permission.upper() == "Y":
        return True
    if permission.upper() == "N":
        return False
    return "your input is not valid"


def modify_todo_list(todo_list, modification_ans):
    if modification_ans.upper() == "ADD":
        name = input("enter task name : ")
        description = input("enter task description : ")
        priority = input("enter task priority : ")
        priority_mapping = {
            "HIGH": Priority.HIGH,
            "MEDIUM": Priority.MEDIUM,
            "LOW": Priority.LOW
        }
        try:
            task = Task(name, description, priority_mapping.get(priority.upper()))
            ToDOList.add(todo_list, task)
            print("task added successfully")
            done = True
        except TypeError as e:
            print("please enter valid input for priority (high, medium, low)")
            done = False
    elif modification_ans.upper() == "REMOVE":
        remove_task_name = input("enter task name : ")

        if todo_list.remove_task_by_name(remove_task_name) is not None:
            print("task removed successfully")
            done = True
        else:
            done = False
    elif modification_ans.upper() == "SHOW":
        ToDOList.show_all_tasks(todo_list)
        done = True
    else:
        print("your answer is not valid")
        done = False
    return done


def save_todo_list(todo_list):
    ToDOList.save_to_output(todo_list)


def upload_todo_list(todo_list: ToDOList):
    ToDOList.upload_from_input(todo_list)
    return todo_list

class ConsoleView:

    @staticmethod
    def run():
        todo_list = make_default_todo_list()
        ans = input("do you want to upload your todolist (from io/input.csv)? (y/n)")
        if check_permission(ans):
            upload_todo_list(todo_list)

        exit_run = False
        while not exit_run:
            done = False
            while not done:
                modification_ans = input("how do you want to modify your todo list? (add, remove, show)")
                done = modify_todo_list(todo_list, modification_ans)

            exit_ans = input("Do you want to exit? (y/n)")
            if check_permission(exit_ans):
                exit_run = True

            pass

        save_ans = input("Do you want to save your todolist? (y/n)")
        if check_permission(save_ans):
            save_todo_list(todo_list)
