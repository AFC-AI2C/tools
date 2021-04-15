#!/bin/bash

# expects an app.py to be mounted into /apps, otherwise it will run the 
# provided app.py in /default/app.py

if [ "$(ls -A /opt/app-root/apps)" ] 
then 
    python /opt/app-root/apps/app.py
else
    python /opt/app-root/default/app.py
fi





