from enums.priority import Priority
from task import Task
from todolist import ToDOList

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
