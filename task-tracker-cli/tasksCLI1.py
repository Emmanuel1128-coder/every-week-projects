import sys

command = sys.argv[1]

if command == 'add':
    task = sys.argv[2]
    tasks = []
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
