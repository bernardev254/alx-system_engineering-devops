#!/usr/bin/python3
"""module that returns an employee todo list progress
"""

import requests
import sys

if __name__ == "__main__":

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

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, tasks))
    print('\n'.join(["\t " + task.get('title') for task in todos.json()]))
