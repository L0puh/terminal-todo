from colorama import Fore
from config import sign_undone, sign_done

def get_done(tasks):
    done=0
    for task in tasks:
        if task[2:5] == '[x]':
            done+=1
    return done

def make_bar(tasks):
    undone_tasks=[]
    done_tasks=[]
    undone = len(tasks)-get_done(tasks)

    for i in range(undone):
        undone_tasks.append(sign_undone)

    for i in range(get_done(tasks)):
        done_tasks.append(sign_done)

    make_print(done_tasks+undone_tasks, undone, tasks)

def make_print(list_tasks, undone, tasks):
    print(Fore.LIGHTCYAN_EX + 'my progress for today:')
    print(Fore.MAGENTA+ ''.join(list_tasks),
            Fore.YELLOW + f'{get_done(tasks)} to {len(tasks)}\n')
