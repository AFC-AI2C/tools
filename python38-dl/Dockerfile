ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=python38-eda
ARG BASE_TAG=latest

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

RUN dnf upgrade -y --nodocs    && \
    dnf install -y gcc gcc-c++ && \
    dnf clean all              && \
    rm -rf /var/cache/dnf/

COPY requirements.txt /opt/python/
RUN python3.8 -m pip install wheel==0.38.2 mmh3==3.0.0
RUN python3.8 -m pip install -r /opt/python/requirements.txt

USER 1001

CMD ["python3"]
