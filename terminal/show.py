from colorama import Fore
from progress_bar import make_bar
from rows import define_row

def make_print(current_row):
    try:
        row, count_row = current_row
        make_bar(row)
        for n, task in enumerate(row):
            print(Fore.MAGENTA + f'{n+1}:', f'{replace_signs(task)}')
    except TypeError:
        print('- there is no such row')

def replace_signs(n):
    if n[2:5] == '[x]':
        color = Fore.GREEN
        text = n.replace(n[:6], color + f'✔ ' + Fore.RESET)
    else:
        color = Fore.RED
        text = n.replace(n[:6], color + '✘ ' + Fore.RESET)
    return text

if '__main__' == __name__:
    make_print(define_row())
