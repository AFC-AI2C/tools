FROM afcai2c/python38

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# nodejs typically installed here to check the status of jlab
# we've removed it due to cve's
# we have also removed bzip2 install as its provided by the python36 base image
# we've removed it and the lang pack installations due to cve's
RUN yum update -yq        && \
    yum install -yq          \
        git                  \
        procps               \
        ca-certificates   && \
    yum clean all

RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER   \
    && chmod -R 775 /home/jovyan                                            

# Install tini
COPY tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

RUN mkdir /opt/jupyter
RUN chown -R jovyan:users /opt/jupyter

USER $NB_UID

# Configure environment
ENV SHELL=/bin/bash         \
    NB_USER=$NB_USER        \
    NB_UID=$NB_UID          \
    NB_GID=$NB_GID          \
    LANG=en_US.UTF-8        \
    LANGUAGE=en_US.UTF-8    \
    HOME=/home/$NB_USER

# configure and install within virtual env for downstream multi-stage build copies

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV VIRTUAL_ENV=/opt/jupyter/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . $VIRTUAL_ENV/bin/activate                             \
    && pip install      \
    pip                                                     \
    jupyterlab                                              \
    jupyterlab-git					    \
    jupyterhub

# for downstream accessibility surrounding jupyterhub 
RUN jupyter serverextension enable --py jupyterlab --sys-prefix

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/work

# critical env variable to enable jupyter lab GUI (default is the old interface)
ENV JUPYTER_ENABLE_LAB=1

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

COPY scripts/start.sh scripts/start-notebook.sh scripts/start-singleuser.sh /usr/local/bin/
COPY scripts/jupyter_server_config.py /etc/jupyter/

USER root

RUN chmod -R 775 /etc/jupyter                       \
    && chmod g-s /usr/libexec/openssh/ssh-keysign

RUN yum remove perl -y

# destroy /usr/share/doc/perl* and tornado test.key as they contain 'secrets' flagged by IB
RUN rm -rf                                                                  \
	/usr/share/doc/perl-IO-Socket-SSL 		                                \
	/usr/share/doc/perl-Net-SSLeay/examples		                            \
	/opt/jupyter/venv/lib/python3.8/site-packages/tornado/test/test.key

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1

WORKDIR $HOME

EXPOSE 8888