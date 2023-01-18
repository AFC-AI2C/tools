ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=python38
ARG BASE_TAG=latest

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

ARG NB_USER="jovyan"
ARG NB_UID="10001"
ARG NB_GID="100"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root
COPY config/*.gpg ./

RUN rpm --import ./NODESOURCE-GPG-SIGNING-KEY-EL.gpg && \
    rm -f ./*.gpg

RUN dnf upgrade -y --nodocs                        && \
    dnf install -y gcc git procps ca-certificates  && \
    dnf module install -y nodejs:16                && \
    dnf clean all                                  && \
    rm -rf /var/cache/dnf

RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    chown -R jovyan /home/jovyan/

# Install tini
COPY tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

RUN mkdir /opt/jupyter/
RUN chown -R jovyan:users /opt/jupyter/

USER $NB_UID

ENV SHELL=/bin/bash         \
    NB_USER=${NB_USER}      \
    NB_UID=${NB_UID}        \
    NB_GID=${NB_GID}        \
    LANG=en_US.UTF-8        \
    LANGUAGE=en_US.UTF-8    \
    HOME=/home/${NB_USER}

# configure and install within virtual env for downstream multi-stage build copies
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV VIRTUAL_ENV=/opt/jupyter/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . $VIRTUAL_ENV/bin/activate && \
    pip install jupyterlab         \
                jupyterlab-git     \
                jupyterhub         \
                ipykernel          \
                nbdime

# for downstream accessibility surrounding jupyterhub
RUN jupyter serverextension enable --py jupyterlab --sys-prefix
RUN jupyter serverextension enable --user jupyterlab_git --sys-prefix

# Setup work directory for backward-compatibility
RUN mkdir /home/${NB_USER}/work

# critical env variable to enable jupyter lab GUI (default is the old interface)
ENV JUPYTER_ENABLE_LAB=1

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

COPY scripts/start.sh scripts/start-notebook.sh scripts/start-singleuser.sh /usr/local/bin/
COPY scripts/jupyter_server_config.py /etc/jupyter/

# begin cleanup and organizing of container
USER root

RUN chown -R jovyan /etc/jupyter/              && \
    chmod -R 0750 /etc/jupyter/                && \
    chown -R jovyan /home/jovyan/              && \
    chmod -R 0750 /home/jovyan/                && \
    chown -R jovyan /opt/jupyter/              && \
    chmod -R 0750 /opt/jupyter/                && \
    chmod g-s /usr/libexec/openssh/ssh-keysign && \
    chmod g-s /usr/bin/write                   && \
    chmod go-w /usr/local/bin/start.sh /usr/local/bin/start-singleuser.sh /usr/local/bin/start-notebook.sh

RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/                     \
           /usr/share/doc/perl-Net-SSLeay/examples/               \
           /opt/jupyter/venv/lib/python3.8/site-packages/tornado/test/

# removal of moment package and files for CVEs but also moment is being deprecated
RUN rm -f /opt/jupyter/venv/share/jupyterhub/static/components/moment/package.json
# update vulnerable npm packages to latest available
RUN npm i -g ansi-regex minimatch

# renames buttons
RUN rm -f /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json   && \
    rmdir $HOME/work
WORKDIR /home/jovyan
COPY kernel.json /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json


# Switch back to jovyan to avoid accidental container runs as root
USER 10001

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
WORKDIR $HOME
EXPOSE 8888


#########
# Usage #
#########

# docker run -p 8888:8888 registry1.dso.mil/ironbank/opensource/jupyter/jupyterlab

# example with enabled authentication token and/or password
# docker run -p 8888:8888 registry1.dso.mil/ironbank/opensource/jupyter/jupyterlab start.sh jupyter lab --LabApp.token='[token-value]' --LabApp.password='[password]'
