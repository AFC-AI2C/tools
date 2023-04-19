ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=python38-eda
ARG BASE_TAG=20230418

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root 

ARG NB_USER="jovyan"
ARG NB_UID="1001"
ARG NB_GID="100"
RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    chown -R jovyan /home/jovyan/

COPY ./scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV HOME=/home/python
ENV VIRTUAL_ENV=/opt/python/venv
ENV PATH="${PATH:+${PATH}:}${VIRTUAL_ENV}/bin"

WORKDIR /home/python
RUN mkdir repo apps scripts
COPY ./scripts/app.py $HOME/app.py

RUN dnf upgrade -y --nodocs && \
    dnf clean all	    && \
    rm -rf /var/cache/dnf

RUN chown -R 1001 /opt/python/

USER 1001

RUN python3.8 -m venv $VIRTUAL_ENV
RUN pip install dash

EXPOSE 8050
ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1
