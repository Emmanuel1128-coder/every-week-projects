import sys
import json
import os
from rich.console import Console
from rich.table import Table

console = Console()

def formatStatus(status):
    if status == 'done':
        return '[green]done[/green]'
    else:
        return '[yellow]todo[/yellow]'

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
elif command == 'list':
    if len(tasks) == 0:
        print('No tasks found.')
    else:
        table = Table(title='My CLI Task Tracker')

        table.add_column('ID', style='#03045e', justify='center')
        table.add_column('Task', style='#0077b6', justify='center')
        table.add_column('Status', style='#00b4d8', justify='center')

        for task in tasks:
            styledStatus = formatStatus(task['status'])
            table.add_row(str(task['id']), task['task'], styledStatus)
        console.print(table)
elif command == 'delete':
    targetID = int(sys.argv[2])
    if targetID > len(tasks):
        print('The ID is out of range.')
    else:
        for task in tasks:
            if task['id'] == targetID:
                tasks.remove(task)
                for i, task in enumerate(tasks, 1):
                    task['id'] = i
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file, indent=4)
                print(f'Task number {targetID} was deleted successfully.')
elif command == "mark-done":
    targetStatus = int(sys.argv[2])
    if targetStatus > len(tasks):
        print('Task number is out of range.')
    else:
        for task in tasks:
            if task['id'] == targetStatus:
                task['status'] = 'done'
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file, indent=4)
                print(f'Task {targetStatus} was updated successfully.')
