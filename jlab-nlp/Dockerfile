FROM afcai2c/jlab-dl:latest

USER root

RUN python3.6 -m pip install  \
    nltk                      \
    gensim                    \
    corenlp                   \
    spacy                     \
    textblob                  \
    patterns                  \
    PyNLPl                    \
    yake                      \
    dateparser                \
    wheel                     \
    flair 

#USER jovyan
USER default

WORKDIR $HOME

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

