FROM afcai2c/python38-ai:latest AS multi-stage
FROM afcai2c/jupyterlab:latest

COPY --from=multi-stage /opt/python /opt/python

# Makes the python packages accessable
ENV PATH="/opt/python/venv/bin:$PATH"

USER root
#Workaround for perl issue preventing yum upgrade
RUN yum remove -y perl-threads
RUN yum upgrade -y     && \
    yum clean all -y   && \
    yum install -y        \
        vim               \
        zip               \
        unzip             \
        net-tools         \
        # gcc is needed for prophet
        gcc-c++           \
        git

# Needed to use packges from multi-stage build in Jupyterlab
RUN python3.8 -m pip install ipykernel

# Removing unneeded vulnerable binaries
RUN yum remove -y    \
    binutils         \
    glibc-devel      \
    glibc-headers    \
    kernel-headers

# Removing identified secret and SUID files
RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/certs/                             && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/                           && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/                           && \
    rm -rf /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem               && \
    rm -rf /opt/python/venv/lib/python3.8/site-packages/tornado/test/test.key   && \
    chmod g-s /usr/libexec/openssh/ssh-keysign

USER jovyan

# Needed to use packges from multi-stage build in Jupyterlab
# A new kernel is displayed and available for use within JupyterLab
RUN python3.8 -m ipykernel install --name='AI_Packages' --user

WORKDIR $HOME

EXPOSE 8888

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1

