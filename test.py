from enums.priority import Priority
from model.task import Task
from model.todolist import ToDOList

if __name__ == '__main__':
    task_1 =  Task("first task", "task 1", priority=Priority.MEDIUM)
    task_2 = Task("second task", "task 2", priority=Priority.HIGH)
    task_3 = Task("third task", "task 3", priority=Priority.LOW)

    task_list = [task_1, task_2, task_3]

    todolist = ToDOList(task_list)

    todolist.show_all_tasks()

    #add task 4
    task_4 = Task("fourth task", "task 4", priority=Priority.MEDIUM)
    todolist.add(task_4)

    #remove task 3
    todolist.remove(task_3)

    print("__________")
    todolist.show_all_tasks()

    print("__________")
    todolist.update_name_of_task("new_name",task_1)
    todolist.update_priority_of_task(priority= Priority.HIGH, task= task_1)
    todolist.update_description_of_task(description= "new description", task= task_1)
    todolist.show_all_tasks()

    print("___________")
    todolist.upload_from_input()
    todolist.show_all_tasks()

    print("___________")
    todolist.save_to_output()
