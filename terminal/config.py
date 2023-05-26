from datetime import date
import os

sign_undone='░'
sign_done='▓'
current_date = date.today().strftime('%d')
current_todo_path = f'todos/{current_date}day.md'
yesterday =int(current_date)-1

def archive_path(day):
    return f'todos/arch/{day}day.md'

def check_existing(path):
    if os.path.exists(path):
        return True
    return False

