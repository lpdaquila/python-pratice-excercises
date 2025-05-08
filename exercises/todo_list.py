import json

FILE_PATH = ''
todo = []
todo_removed = []

def read(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('Error: File not found')
    return data

def save(tasks, file_path):
    data = tasks
    with open(file_path, 'w') as file:
        data = json.dump(tasks, file, ident=2, ensure_ascii=False)
    return data

def list_tasks(tasks):
    print()
    if not tasks:
        print('No tasks to list.')
        return
    
    print('Tasks')
    for task in tasks:
        print('\t- %s' % task)
        
def remove_task(tasks, tasks_removed):
    if not tasks:
        print("There's no tasks to remove.")
        return
    task = tasks.pop()
    print('Task %s has been removed.' % task)
    list_tasks(tasks)
    tasks_removed.append(task)
    
def reuse_task(tasks, tasks_removed):
    if not tasks:
        print("There's no tasks to reuse.")
        return
    task = tasks_removed.pop()
    print('Task %s has been reused.' % task)
    list_tasks(tasks)
    tasks.append(task)
    
def add_task(task, tasks):
    tasks.append(task)
    print('Task "%s" added successfully.' % task)
    list_tasks(tasks)

while True:
    print()
    print('Commands: ls (list), rm (remove), ru (reuse)')
    task = input('Type a task or a command: ')
    
    commands = {
        'ls': lambda: list_tasks(todo),
        'rm': lambda: remove_task(todo, todo_removed),
        'ru': lambda: reuse_task(todo, todo_removed),
        'add': lambda: add_task(task, todo),
    }
    
    command = commands.get(task) if commands.get(task) \
        is not None else commands['add']
    command()
    save(todo, FILE_PATH)
    
