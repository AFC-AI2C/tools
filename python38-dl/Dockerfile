ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=python38-eda
ARG BASE_TAG=latest

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

RUN dnf upgrade -y         && \
    dnf clean all          && \
    rm -rf /var/cache/dnf

COPY requirements.txt /opt/python/

USER 1001

ENV VIRTUAL_ENV=/opt/python/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install -r /opt/python/requirements.txt

USER 1001
WORKDIR $HOME
HEALTHCHECK --interval=10s --timeout=1s CMD python3.8 -c 'print("up")' || exit 1
