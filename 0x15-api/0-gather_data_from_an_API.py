#!/usr/bin/python3
"""Python script that, using this REST API, for a given
   employee ID, returns information about his/her TODO list progress.
"""

if name == "__main__":
    import requests
    import sys

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
