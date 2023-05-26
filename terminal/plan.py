import sys
from config import current_date

arg = sys.argv[1:]

def get_date_plan(arg):
    try:
        return arg[1]
    except:
        tomorrow_date=int(current_date)+1
        return tomorrow_date

def make_plan(date_plan):
    with open(f'todos/cache/{date_plan}.txt', 'a') as f:
        f.write(f'- [ ] {arg[0]}\n')

if '__main__' == __name__:
    make_plan(get_date_plan(arg))


