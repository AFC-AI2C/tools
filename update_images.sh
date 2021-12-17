#! /bin/bash

for file in */ ; do 
    if [[ -d "$file" && ! -L "$file" ]]; then
        #cat "./$file/Dockerfile"| head -n 1
        # echo $file
        #echo $file | tr '/' ' ' 

        # Replaces the slash at the end of the string
        name=${file//[\/]/}

        # Builds Docker images
        eval "docker build -t 'afcai2c/$name' --no-cache './$name'"

        # Commit update to github
        # NOT NEEDED, MAY USE LATER...
        # git add "./$name"
        # git commit -m "Updated packages in $name"
        # git push origin main

        eval "docker push 'afcai2c/$name:latest'"
    fi
done


