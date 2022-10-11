FROM afcai2c/python38-ai:latest AS multi-stage
FROM afcai2c/jupyterlab:latest

COPY --from=multi-stage /opt/python /opt/python

# Makes the python packages accessable
ENV PATH="/opt/python/venv/bin:$PATH"

USER root
#Workaround for perl issue preventing yum upgrade
RUN dnf upgrade -y --nodocs && \
    dnf install -y             \
        vim                    \
        zip                    \
        unzip                  \
        net-tools              \
      # gcc is needed for prophet
        gcc-c++                \
        gcc                    \
        git                 && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

# Needed to use packges from multi-stage build in Jupyterlab
RUN python3.8 -m pip install ipykernel

# Removing unneeded vulnerable binaries
RUN dnf remove -y    \
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

RUN usermod -u 1002 python  && \
    usermod -u 1001 jovyan

USER root

# The following does not produce the desired results
  # jupyter kernelspec uninstall python3 -y
  # jupyter kernelspec list
# No longer needed, modified kernel.json file instead
  # python3.8 -m ipykernel install --name='AI_Packages' --display-name 'Python3.8 (AI_Packages)' --user

RUN rm -f /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json   && \
    rmdir $HOME/work


COPY ./files/kernel.json /opt/jupyter/venv/share/jupyter/kernels/python3/kernel.json
COPY ./files/README.md .

# Start VS Code
USER root
RUN cd ~
RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN echo "/bin/code-server --bind-addr 0.0.0.0:8080 --auth none --cert false &" >> ./start-notebook.sh

WORKDIR /home/jovyan

USER 1001

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1






EXPOSE 8080
