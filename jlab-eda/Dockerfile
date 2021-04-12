# ARG BASE_REGISTRY=registry1.dso.mil
# ARG BASE_IMAGE=ironbank/redhat/python/python36
# ARG BASE_TAG=3.6
# FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM dmedina7301/python36:latest

ARG NB_USER="jovyan"
# NB_UID == 1001 b/c the default user in the ironbank python36 image is uid 1001
ARG NB_UID="1000"
ARG NB_GID="0"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# nodejs typically installed here to check the status of jlab
# we've removed it due to cve's
# we have also removed bzip2 install as its provided by the python36 base image
# we have also removed the lang pack installations due to cve's
RUN yum update -y -q && \
    yum install -y -q \
        procps \
        ca-certificates && \
    yum clean all

# Configure environment
ENV SHELL=/bin/bash       \
    NB_USER=$NB_USER      \
    NB_UID=$NB_UID        \
    NB_GID=$NB_GID        \
    LANG=en_US.UTF-8      \
    LANGUAGE=en_US.UTF-8
ENV HOME=/home/$NB_USER

# Copy a script that we will use to correct permissions after running certain commands
# fix-permissions: https://repo1.dsop.io/dsop/redhat/python/python36/-/blob/development/scripts/usr/bin/fix-permissions
COPY scripts/fix-permissions /usr/local/bin/fix-permissions
RUN chmod a+rx /usr/local/bin/fix-permissions

# Enable prompt color in the skeleton .bashrc before creating the default NB_USER
# hadolint ignore=SC2016
RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/' /etc/skel/.bashrc

# Create NB_USER with name jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER &&    \
    fix-permissions $HOME -P &&                                     \
    fix-permissions /opt/app-root -P

# install tini
COPY tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

USER $NB_UID

ARG PYTHON_VERSION=default

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/work

WORKDIR /tmp

RUN python3.6 -m pip install jupyterlab && \
    fix-permissions /opt/app-root


EXPOSE 8888

# critical env variable to enable jupyter lab GUI (default is the old interface)
ENV JUPYTER_ENABLE_LAB=1
# Configure container startup
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

# Copy local files as late as possible to avoid cache busting
COPY scripts/start.sh scripts/start-notebook.sh scripts/start-singleuser.sh /usr/local/bin/
COPY scripts/jupyter_notebook_config.py /etc/jupyter/

# Fix permissions on /etc/jupyter and /usr/libexec/openssh/ssh-keysign
USER root

RUN chmod +x /usr/local/bin/start-notebook.sh

RUN fix-permissions /etc/jupyter && \
    fix-permissions /usr/libexec/openssh/ssh-keysign

# destroy /usr/share/doc/perl* and tornado test.key as they contain 'secrets' flagged by IB
RUN rm -rf \
	/usr/share/doc/perl-IO-Socket-SSL 		    \
	/usr/share/doc/perl-Net-SSLeay/examples		\
	/opt/app-root/lib/python3.6/site-packages/tornado/test/test.key

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1

WORKDIR $HOME