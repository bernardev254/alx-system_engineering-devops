#!/usr/bin/python3
"""export data in the CSV format.
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    emp_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(emp_id))
    name = user.json()[0].get('username')

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id))
    my_file = emp_id + '.csv'
    with open(my_file, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            writer.writerow([emp_id, name, str(task.get('completed')),
                            task.get('title')])
