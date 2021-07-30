Data Science starts with data.
Label Studio removes the pain labeling it.

# STARTING LABEL STUDIO
Pass in credentials into container - login using them 
    docker run -it --rm -p 8080:8080 -e LABEL_STUDIO_USERNAME='username@example.com' -e LABEL_STUDIO_PASSWORD='password' afcai2c/label-studio:latest

# DATA PERSISTENCE
Below are exmples commands for data persistence.
    docker run -it -p 8080:8080 -v <yourvolume>:/label-studio/data label-studio:latest
    docker run -it -p 8080:8080 -v `pwd`/mydata:/label-studio/data label-studio:latest label-studio --log-level DEBUG
