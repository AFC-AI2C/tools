FROM afcai2c/python38-nlp AS multi-stage

FROM redhat/ubi8:latest

ENV PATH="/usr/lib/python3.8/site-packages:$PATH"

USER root

ARG NB_USER="lumi"
ARG NB_UID="1001"
ARG NB_GID="100"

RUN dnf upgrade -y --nodocs          && \
    dnf install -y curl vim python38 && \
    dnf clean all                    && \
    rm -rf /var/cache/dnf

RUN mkdir -p /.config/
RUN cd ~
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    chown -R lumi:users /.config/

COPY --from=multi-stage /opt/python/venv/lib/python3.8/site-packages/ /usr/lib/python3.8/site-packages/

RUN chmod -R 0750 /usr/lib/ && \
    chmod -R 0750 /usr/local/bin/ && \
    chmod -R 0750 /usr/local/lib/ && \
    chmod -R 0750 /usr/local/lib64/ && \
    chown -R lumi /usr/lib/ && \
    chown -R lumi /usr/local/lib/ && \
    chown -R lumi /usr/local/lib64/ && \
    chown -R lumi /usr/local/bin/

USER $NB_UID
EXPOSE 8080
ENTRYPOINT ["/bin/code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--cert", "false"]
