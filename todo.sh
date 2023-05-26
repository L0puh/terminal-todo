# ! /usr/bin/zsh
cd "YOUR PATH/todos/"
if [ $# -eq 0 ]
then
    # arg was not given
    python main.py
elif [ $1 = "open" ]
then
    # open current todo list
    python terminal/open_file.py $2
elif [ $1 = "show" ]
then
    python terminal/show.py $2 

elif [ $1 = "check-off" ]
then
    python terminal/show.py 
    python terminal/check_off.py  
elif [ $1 = "add" ]
then
    python terminal/show.py $2
    python terminal/add_task.py $2

elif [ $1 = "get-started" ]
then 
    python get_started.py
else
    # plan to given date
    python terminal/plan.py $1 $2
fi
