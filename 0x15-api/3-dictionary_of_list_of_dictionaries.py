#!/usr/bin/python3
"""export data in the json format.
"""
import requests
import json
if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    my_file = 'todo_all_employees.json'
    users_dict = {}
    for user in users.json():
        emp_id = user.get('id')
        name = user.get('username')
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(emp_id))
        tasks_list = []
        for task in todos.json():
            task_dict = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            tasks_list.append(task_dict)
        users_dict[emp_id] = tasks_list
    with open(my_file, mode='w') as f:
        json.dump(users_dict, f)
