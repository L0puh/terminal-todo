import os, datetime
from pathlib import Path
from terminal.config import current_todo_path, current_date,\
        yesterday, archive_path, check_existing

def get_template():
    with open('template.md', 'r') as f:
        file=f.read()
    return file

def create_file():
    if not check_existing(current_todo_path):
        with open(current_todo_path, 'a') as f:
            f.write(f'*day {current_date}/31*\n' + get_template())
        check_for_cache()

def move_to_arch():
    yest_file=f"todos/{yesterday}day.md"
    path_cache=f'todos/cache/{yesterday}.txt'

    if check_existing(yest_file):
        Path(yest_file).rename(archive_path(yesterday))
    else: print('- yesterday is missing')

    if check_existing(path_cache):
        os.remove(path_cache)
        print('+ removed cache')

def check_for_cache():
    file=f'todos/cache/{current_date}.txt'
    if check_existing(file):
        with open(file, 'r') as f:
            file = f.read()

        with open(current_todo_path, 'a') as f:
            f.write('\n# plans:\n' + file)

if '__main__'==__name__:
    create_file()
    move_to_arch()
