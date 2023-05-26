import sys
from rows import get_lines, get_rows
from check_off import rewrite_file

lines = get_lines()

def take_input():
    input_task = input('input: ')

    lists=[x[1] for x in get_rows()]
    count=lists[int(sys.argv[1:][0])-1]
    for i in get_rows():
        if int(i[1]) == int(count):
            changes =  f'- [ ] {input_task}\n'
            return  lines[:int(i[1])+1]\
                    +changes.split('0')\
                    +lines[int(i[1])+2:]

if '__main__' == __name__:
    rewrite_file(take_input())
