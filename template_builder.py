def get_amount_rows():
    names=[]
    rows = int(input("how many rows?: "))
    for i in range(1, rows+1):
        names.append(input(f'name for {i} row: '))
    return names

def make_template():
    with open('template.md', 'w') as f:
        [f.write(f'# {i}\n- [ ]\n\n') for i in get_amount_rows()]

if "__main__" == __name__:
    make_template()
