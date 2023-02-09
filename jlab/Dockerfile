### set base image
ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=python38
ARG BASE_TAG=20230209il5

#### use base image
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

### start with root
USER root

### add user Jovyan/1001 because that's how coeus is hard-coded
ARG NB_USER="jovyan"
ARG NB_UID="1001"
ARG NB_GID="100"
RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    chown -R jovyan /home/jovyan/

### allows for package install from EPEL
COPY config/*.gpg ./
RUN rpm --import ./NODESOURCE-GPG-SIGNING-KEY-EL.gpg && \
    rm -f ./*.gpg

### upgrades base packages and installs some more base packages
RUN dnf upgrade -y --nodocs                        && \
    dnf install -y gcc git procps ca-certificates  && \
    dnf module install -y nodejs:16                && \
    dnf clean all                                  && \
    rm -rf /var/cache/dnf

### installs yarn
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
    dnf install -yq yarn

### installs tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

### creates directory where jupyter venv will be hosted
RUN mkdir /opt/jupyter/
RUN chown -R jovyan:users /opt/jupyter/

### swaps to user jovyan for setting up and installing jlab venv packages
USER 1001

### environment variables for common use
ENV SHELL=/bin/bash         \
    NB_USER=${NB_USER}      \
    NB_UID=${NB_UID}        \
    NB_GID=${NB_GID}        \
    LANG=en_US.UTF-8        \
    LANGUAGE=en_US.UTF-8    \
    HOME=/home/${NB_USER}

### configure and install within virtual env for downstream multi-stage build copies
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV VIRTUAL_ENV=/opt/jupyter/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.8 -m venv $VIRTUAL_ENV
RUN . $VIRTUAL_ENV/bin/activate && 	          \
    pip install --upgrade pip wheel setuptools && \
    pip install jupyterlab         	          \
                jupyterlab-git    	          \
                jupyterhub                        \
                ipykernel                         \
                nbdime                            \
		jupyterlab-lsp 			  \
        	lckr-jupyterlab-variableinspector \
        	neptune-notebooks 		  \
		jupyterlab-system-monitor 	  \
        	nbdime	 			  \
        	ipywidgets 			  \
        	jupyter_bokeh 			  \
        	jupyter-dash 			  \
        	jupyterlab-templates 		  \
        	ipympl 				  \
        	jupytext 			  \
        	jupyterlab_tabnine 		  \
        	jupyterlab-drawio 		  \
      		jupyterlab-tabular-data-editor 	  \
        	jupyterlab-snippets 		  \
        	jupyterlab-tensorboard-pro
                
### installs jupyetlab_sql server extension
RUN pip install jupyterlab_sql 					    && \
    jupyter serverextension enable jupyterlab_sql --py --sys-prefix && \
    jupyter lab build

### for downstream accessibility surrounding jupyterhub and prevents git extension error
RUN jupyter serverextension enable --py jupyterlab --sys-prefix
RUN jupyter serverextension enable --user jupyterlab_git --sys-prefix

### installs more extensions
RUN jupyter labextension install \
    @jupyterlab/toc 		 \
    @jupyterlab/celltags 	 \
    jupyterlab-spreadsheet

### Setup work directory for backward-compatibility
RUN mkdir /home/${NB_USER}/work

### critical env variable to enable jupyter lab GUI (default is the old interface)
ENV JUPYTER_ENABLE_LAB=1

COPY scripts/start.sh scripts/start-notebook.sh scripts/start-singleuser.sh /usr/local/bin/
COPY scripts/jupyter_server_config.py /etc/jupyter/

### use root to clean up and organize container
USER root

### permission fuckfest because reasons - will come back to this
RUN chown -R jovyan /etc/jupyter/              && \
    chmod -R 0750 /etc/jupyter/                && \
    chown -R jovyan /home/jovyan/              && \
    chmod -R 0750 /home/jovyan/                && \
    chown -R jovyan /opt/jupyter/              && \
    chmod -R 0750 /opt/jupyter/                && \
    chmod g-s /usr/libexec/openssh/ssh-keysign && \
    chmod g-s /usr/bin/write                   && \
    chmod go-w /usr/local/bin/start.sh /usr/local/bin/start-singleuser.sh /usr/local/bin/start-notebook.sh

### renames jlab extensions to include AI_PACKAGES
RUN rm -f /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json
COPY kernel.json /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json

### switches back to jovyan to avoid container runs as root
USER 1001

ENTRYPOINT ["/tini", "-g", "--"]
CMD ["start-notebook.sh"]
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
WORKDIR ~
EXPOSE 8888


#########
# Usage #
#########

# docker run -p 8888:8888 registry1.dso.mil/ironbank/opensource/jupyter/jupyterlab

# example with enabled authentication token and/or password
# docker run -p 8888:8888 registry1.dso.mil/ironbank/opensource/jupyter/jupyterlab start.sh jupyter lab --LabApp.token='[token-value]' --LabApp.password='[password]'
