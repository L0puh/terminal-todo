import subprocess
import sys, os
from config import check_existing, archive_path, current_date

date_arg = sys.argv[1:2]

def check_date(date_arg):
    try: open_file(date_arg[0])
    except: open_file(current_date)


def open_file(day):
    if check_existing(archive_path(day)):
        subprocess.run(['nvim', archive_path(day)])
    elif check_existing(f'todos/{day}day.md'):
        subprocess.run(['nvim', f'todos/{day}day.md'])
    else:
        print('there is no such file...')

if '__main__' == __name__:
    check_date(date_arg)

