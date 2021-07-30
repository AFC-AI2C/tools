FROM afcai2c/jlab-dl:latest

USER root

RUN dnf update -y          && \
    dnf clean all -y

RUN python3.8 -m pip install  \
    wheel        \
    flair        \
    nltk         \
    gensim       \
    corenlp      \
    spacy        \
    textblob     \
    patterns     \
    PyNLPl       \
    yake         \
    dateparser

RUN rm -f /opt/python/venv/lib/python3.8/site-packages/future/backports/test/badcert.pem          \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/badkey.pem           \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/keycert2.pem         \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/keycert.passwd.pem   \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/keycert.pem          \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/ssl_key.passwd.pem   \
          /opt/python/venv/lib/python3.8/site-packages/future/backports/test/ssl_key.pem

USER jovyan

WORKDIR $HOME

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1
