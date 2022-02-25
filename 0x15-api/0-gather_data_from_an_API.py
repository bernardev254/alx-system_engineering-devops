#!/usr/bin/python3
"""Module that returns information about employee's TODO list progress.
"""

import requests
import sys

if name == "__main__":

    emp_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(emp_id))
    name = user.json()[0].get('name')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id))
    tasks = len(todos.json())
    completed = 0

    for task in todos.json():
        if task.get('completed'):
            completed += 1

    print("Employee {} is done with task ({}/{})"
          .format(name, completed, tasks))
    print('\n'.join(["\t" + task.get('title') for task in todos.json()]))