#ARG BASE_REGISTRY=registry1.dso.mil
#ARG BASE_IMAGE=ironbank/carnegie-mellon/jlab-dl
#ARG BASE_TAG=3.6
#FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c\jlab-dl:latest

USER root

#RUN yum update -y -q && \
#    yum install -y -q \

WORKDIR /tmp/repo

COPY *.whl .
COPY *.tar.gz .
COPY *.zip .

RUN python3.6 -m pip install --no-index --find-links . \
    nltk \
    gensim \
    corenlp \
    spacy \
    textblob \
    patterns \
    PyNLPl \
    yake \
    dateparser \
    # wheel updated for flair to work
    wheel \
    flair 

RUN rm -rf /tmp/repo

USER jovyan

WORKDIR $HOME

#ENTRYPOINT ["bash"]
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

##################
# Testing Packages


##################
# Packages Not Installed Notes
