# ARG BASE_REGISTRY=registry1.dso.mil
# ARG BASE_IMAGE=ironbank/carnegie-mellon/jlab-dl
# ARG BASE_TAG=3.6
# FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c/jlab-dl:latest

USER root

RUN curl -LO http://13.89.34.249/graphviz-devel.tar.gz
RUN tar xvf graphviz-devel.tar.gz
RUN yum update -y && yum localinstall -y ./graphviz-devel/*.rpm

RUN python3.6 -m pip install \
    decorator                                          \
    python-igraph                                      \
    networkx                                           \
    scikit_network                                     \
    numpy                                              \
    scipy                                              \
    texttable                                          \
    pygraphviz 

USER jovyan

WORKDIR $HOME

#ENTRYPOINT ["bash"]
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

