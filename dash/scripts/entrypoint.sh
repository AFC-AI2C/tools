#!/bin/bash

# expects your custom app.py to be mounted into /home/python3/apps, otherwise it
# will run the provided app.py in /home/python3/app.py

if [ -e $HOME/apps/app.py ] 
then 
    echo "running mounted application.."
else
    echo "pre-loading app.py"
    cp $HOME/app.py apps/
fi

cd $HOME/apps
python app.py
