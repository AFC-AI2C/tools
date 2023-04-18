ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=python38-dl
ARG BASE_TAG=20230418

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

RUN dnf upgrade -y --nodocs && \
    dnf clean all           && \
    rm -rf /var/cache/dnf/

COPY requirements.txt /opt/python/

USER 1002

ENV VIRTUAL_ENV=/opt/python/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3.8 -m venv $VIRTUAL_ENV
RUN pip install -r /opt/python/requirements.txt

CMD ["python3"]
