#! /bin/bash

superset fab create-admin --firstname '' --lastname '' --email '' --username "$USERNAME" --password "$PASSWORD" 

#superset load-test-users
#superset load-examples
#superset set-database-usi 

superset init

superset run --host 0.0.0.0 -p 8088 --with-threads --reload --debugger