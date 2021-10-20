#!/bin/bash

# expects your custom app.py to be mounted into /home/python3/apps, otherwise it
# will run the provided app.py in /home/python3/app.py

if [ "$(ls -A $HOME/apps)" ] 
then 
    echo "running mounted application.."
    cd $HOME/apps
else
    cd $HOME
fi

python app.py
