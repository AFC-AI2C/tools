ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=python38
ARG BASE_TAG=20230209il5

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG} as build

USER root

RUN dnf upgrade -y --nodocs    && \
    dnf install -y gcc gcc-c++ && \
    dnf clean all              && \
    rm -rf /var/cache/dnf/

ENV VIRTUAL_ENV=/opt/python/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /opt/python/
RUN chown -R 1002 /opt/python/

USER 1002

RUN python3.8 -m venv $VIRTUAL_ENV
RUN pip install -r /opt/python/requirements.txt

CMD ["python3"]


