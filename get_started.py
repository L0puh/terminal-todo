import os
from terminal.config import check_existing
from template_builder import make_template

def create_dirs():
    todos=check_existing('todos/')
    cache=check_existing('todos/cache')
    arch=check_existing('todos/arch')
    if not todos and not cache and not arch:
        os.mkdir('todos')
        os.mkdir('todos/cache')
        os.mkdir('todos/arch')

if '__main__' == __name__:
    create_dirs()
    make_template()
