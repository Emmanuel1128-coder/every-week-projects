import sys
import json
import os

command = sys.argv[1]

if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
else:
    tasks = []

if command == 'add':
    task = sys.argv[2]
    if len(tasks) == 0:
        nextID = 1
    else:
        nextID = len(tasks) + 1
    newTask = {
        'id': nextID,
        'task': task,
        'status': 'todo'
    }
    print('Task added:', newTask)
    tasks.append(newTask)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
