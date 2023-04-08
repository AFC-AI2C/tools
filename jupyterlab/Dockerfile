FROM afcai2c/python38

ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

RUN dnf upgrade -y --nodocs         && \
    dnf install -y                     \
        git                            \
        procps                 	       \
        ca-certificates     	    && \
    dnf module install -y nodejs:16 && \
    dnf clean all	    	    && \
    rm -rf /var/cache/dnf
    
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo   && \
    dnf install -yq yarn

RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER   && \
    chmod -R 775 /home/jovyan                                            

# Install tini
#RUN curl -L http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/tini --output /usr/local/bin/tini
COPY ./tini /usr/local/bin/tini

RUN chmod +x /usr/local/bin/tini

RUN mkdir /opt/jupyter && \
    chown -R jovyan:users /opt/jupyter

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
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3.8 -m venv $VIRTUAL_ENV
RUN . $VIRTUAL_ENV/bin/activate   && \
    pip install \
        pip \
        jupyterlab \
        jupyterhub \
# https://github.com/jupyterlab/jupyterlab-git
        jupyterlab-git \
# https://github.com/krassowski/jupyterlab-lsp
        jupyterlab-lsp \
# https://github.com/lckr/jupyterlab-variableInspector
        lckr-jupyterlab-variableinspector \
# https://docs.neptune.ai/tools/jupyter/installing_extension/
        neptune-notebooks \
# https://github.com/jtpio/jupyterlab-system-monitor
	    jupyterlab-system-monitor \
# https://github.com/jupyter/nbdime
        nbdime \
# https://github.com/jupyter-widgets/ipywidgets#ipywidgets-interactive-html-widgets
        ipywidgets \
# https://github.com/bokeh/jupyter_bokeh
        jupyter_bokeh \
# https://github.com/plotly/jupyter-dash
        jupyter-dash \
# https://pypi.org/project/jupyterlab-templates/
        jupyterlab-templates \
# https://github.com/matplotlib/ipympl
        ipympl \
# https://github.com/mwouts/jupytext/
        install jupytext \
# https://www.tabnine.com/install/jupyterlab
        jupyterlab_tabnine \
# https://github.com/QuantStack/jupyterlab-drawio
# RUN jupyter labextension install jupyterlab-drawio
        jupyterlab-drawio \
# https://pypi.org/project/jupyterlab-tabular-data-editor
        jupyterlab-tabular-data-editor \
# https://github.com/QuantStack/jupyterlab-snippets
        jupyterlab-snippets \
# https://pypi.org/project/jupyterlab-tensorboard-pro/
        jupyterlab-tensorboard-pro

# https://github.com/pbugnion/jupyterlab-sql
RUN pip install jupyterlab_sql && \
    # for downstream accessibility surrounding jupyterhub 
    jupyter serverextension enable jupyterlab_sql --py --sys-prefix && \
    jupyter lab build

RUN jupyter labextension install \
# https://github.com/jupyterlab/jupyterlab-toc
    @jupyterlab/toc \
# https://github.com/jupyterlab/jupyterlab-celltags
    @jupyterlab/celltags \
# https://github.com/quigleyj97/jupyterlab-spreadsheet
    jupyterlab-spreadsheet

### START - Currently not supported
# https://github.com/jupyterlab/jupyterlab-google-drive
# RUN jupyter labextension install @jupyterlab/google-drive
# https://github.com/altair-viz/jupyterlab_voyager
# RUN jupyter labextension install jupyterlab_voyager
# https://github.com/mflevine/jupyterlab_html
# RUN jupyter labextension install @mflevine/jupyterlab_html
# https://www.npmjs.com/package/@jupyterlab/plotly-extension
# RUN jupyter labextension install @jupyterlab/plotly-extension
# https://github.com/microsoft/gather
# RUN jupyter labextension install nbgather
# https://github.com/jupyterlab/debugger
# RUN jupyter labextension install jupyterlab/debugger
# https://github.com/chaoleili/jupyterlab_tensorboard
# RUN pip install jupyterlab_tensorboard
### END - Currently not supported


# critical env variable to enable jupyter lab GUI (default is the old interface)
ENV JUPYTER_ENABLE_LAB=1

COPY ./kernel.json /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json
COPY ./scripts/start.sh ./scripts/start-notebook.sh ./scripts/start-singleuser.sh /usr/local/bin/
COPY ./scripts/jupyter_server_config.py /etc/jupyter/

USER root

RUN chmod -R 775 /etc/jupyter                   && \
    chmod g-s /usr/libexec/openssh/ssh-keysign  && \
    chmod go-w /usr/local/bin/start.sh /usr/local/bin/start-singleuser.sh /usr/local/bin/start-notebook.sh

RUN dnf remove perl -y

# destroy /usr/share/doc/perl* and tornado test.key as they contain 'secrets' flagged by IB
RUN rm -rf                                                                  \
	/usr/share/doc/perl-IO-Socket-SSL 		                                \
	/usr/share/doc/perl-Net-SSLeay/examples		                            \
	/opt/jupyter/venv/lib/python3.8/site-packages/tornado/test/test.key

USER $NB_UID

WORKDIR /home/$NB_USER

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1 

EXPOSE 8888
