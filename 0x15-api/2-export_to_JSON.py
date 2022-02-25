#!/usr/bin/python3
"""export data in the json format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    emp_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(emp_id))
    name = user.json()[0].get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id))
    my_file = emp_id + '.json'
    user_dict = {}
    tasks_list = []

    for task in todos.json():
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        tasks_list.append(task_dict)
    user_dict[emp_id] = tasks_list
    with open(my_file, mode='w') as f:
        json.dump(user_dict, f)
