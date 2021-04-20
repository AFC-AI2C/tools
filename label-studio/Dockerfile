#ARG BASE_REGISTRY=registry1.dso.mil
#ARG BASE_IMAGE=ironbank/redhat/python/python36
#ARG BASE_TAG=3.6
#FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c/python38-ai:latest

# changing from root to default user 
USER default

RUN python3.8 -m pip install label-studio 

#ENV LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true

USER root
RUN ln -s /home/default/.local/bin/label-studio /bin

USER default

#ENTRYPOINT ["label-studio","start","My First Label Project","--init","--username","user@army.mil","--password","1234qwer!@#$QWER"]
ENTRYPOINT ["label-studio","start","--log-level","DEBUG"]

# DATA PERSISTENCE
##docker run -it -p 8080:8080 -v <yourvolume>:/label-studio/data label-studio:latest
##docker run -it -p 8080:8080 -v `pwd`/mydata:/label-studio/data label-studio:latest label-studio --log-level DEBUG

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

