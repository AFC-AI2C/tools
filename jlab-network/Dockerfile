FROM afcai2c/jlab-dl:latest

USER root

RUN curl -LO http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/graphviz-devel.tar.gz   && \
    tar xvf graphviz-devel.tar.gz                        && \
    yum localinstall -y ./graphviz-devel/*.rpm           && \
    yum install -y gcc

RUN python3.8 -m pip install     \
        decorator                \
        python-igraph            \
        networkx                 \
        scikit_network           \
        texttable                \
        pygraphviz 

RUN yum remove -y gcc                     && \
    rm -rf /home/jovyan/graphviz-devel*   && \
    . $VIRTUAL_ENV/bin/activate

USER 1001

WORKDIR /home/jovyan

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]
# start-notebook.sh inherited from ironbank/opensource/jupyter/jupyterlab 
# https://repo1.dso.mil/dsop/opensource/jupyter/jupyterlab/-/blob/development/scripts/start-notebook.sh

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1
