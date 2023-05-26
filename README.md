## stack:
- datetime, subprocess (built-in libs)
- colorama
- python, bash 
## how to use:
#### 1. Get started 
1. Put the path of the shell script in your bash 
```bash
alias todo='bash YOUR PATH\todo.sh'
```
2. Put the path of your directory in `todo.sh`
```bash
cd "YOUR-PATH"
```
3. Make the basic template 
```bash
python get_started.py
``` 
4. Create todo file for a current day
```bash
todo
```

#### 2. Make a plan for a month 
```bash
todo "{task}" {date}
todo "buy eggs" 12
```
> if you won't mention a date, it'll be replaced by tomorrow

### 3. Open current day
Open todo list in markdown for a current day with:
```bash
todo open
```
or some previous one 
```bash
todo open {date}
```
> files open in nvim by default

#### 4. Show your list in a terminal
```bash
todo show {row}
```
`row` is a section of your todo list, defined in the template. without mention of row all tasks will be shown
#### 5. Check off a task 
```bash
todo check-off 
```
then type a task number

#### 6. Add a new task
```bash 
todo add {row}
```
then type a task

## FIX:
- [ ] month in a template 
