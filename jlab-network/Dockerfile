FROM afcai2c/jlab-dl:latest

USER root

RUN dnf install -y graphviz gcc && \
    dnf --enablerepo=powertools install -y graphviz-devel && \
    dnf clean all               && \
    rm -rf /var/cache/dnf

RUN python3.8 -m pip install     \
        decorator                \
        python-igraph            \
        networkx                 \
        scikit_network           \
        texttable                \
        pygraphviz               \
        scapy

RUN dnf remove -y gcc && \
    . $VIRTUAL_ENV/bin/activate

USER 1001

WORKDIR /home/jovyan

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]
# start-notebook.sh inherited from ironbank/opensource/jupyter/jupyterlab 
# https://repo1.dso.mil/dsop/opensource/jupyter/jupyterlab/-/blob/development/scripts/start-notebook.sh

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1
