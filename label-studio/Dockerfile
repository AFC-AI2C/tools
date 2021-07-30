FROM afcai2c/python38-ai:latest

ARG LABEL_STUDIO_USERNAME
ARG LABEL_STUDIO_PASSWORD

USER 1001

RUN python3.8 -m pip install label-studio 

#ENV LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true

USER root

RUN ln -s /home/default/.local/bin/label-studio /bin

USER 1001

ENV LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true

# STARTING LABEL STUDIO
# docker run -it --rm -p 8080:8080 -e LABEL_STUDIO_USERNAME='username@example.com' -e LABEL_STUDIO_PASSWORD='password' afcai2c/label-studio:latest

ENTRYPOINT ["label-studio","start","--log-level","DEBUG"]

# DATA PERSISTENCE
##docker run -it -p 8080:8080 -v <yourvolume>:/label-studio/data label-studio:latest
##docker run -it -p 8080:8080 -v `pwd`/mydata:/label-studio/data label-studio:latest label-studio --log-level DEBUG

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

