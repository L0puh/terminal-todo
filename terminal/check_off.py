import sys, fileinput
from rows import define_row, get_rows, get_lines
from config import current_todo_path

tasks, count_row = define_row()
lines = get_lines()

def replace_task(choice):
    for n, line in enumerate(tasks):
        if n+1 == choice:
            task = line
    for n, line in enumerate(lines):
        if line == task:
            sign='[x]'
            if line[2:5] == '[x]': sign = '[ ]'
            change = line.replace(line, f'- {sign} {line[6:]}').split('///')
            return lines[:n] + change + lines[n+1:]

def check_off():
    number = int(input("input: "))
    rewrite_file(replace_task(number))

def rewrite_file(text):
    file = open(current_todo_path, 'w')
    for i in text:
        file.write(f'{i}\n')

if '__main__'==__name__:
    check_off()
