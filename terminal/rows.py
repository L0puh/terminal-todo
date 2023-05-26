import re, sys
from config import current_todo_path

args = sys.argv[1:]

def get_lines():
    with open(current_todo_path, 'r') as f:
        lines = re.split('\n', f.read())
    return lines

def get_rows():
    chunk=[]
    for n, row in enumerate(make_list(get_lines())):
        if row == '':
            yield chunk, n
            chunk=[]
        else: chunk.append(row)
    yield chunk, n

def define_row():
    count_row=0
    try:
        for row in get_rows():
            count_row+=1
            if count_row==int(args[0]) and row[0]:
                res =[True for l in row[0] if l[:1] == '-']
                if res: return row[0][1:], count_row
    except IndexError:
        lists = [i[0][1:] for i in get_rows()]
        lists = [l for i in lists for l in i if l[:1] == '-']
        return lists, count_row

def make_list(lines):
    rows=[]
    for line in lines[1:]:
        rows.append(line)
    return rows
