from redhat/ubi8:latest

USER root

ARG NB_USER="lumi"
ARG NB_UID="1001"
ARG NB_GID="100"

RUN dnf upgrade -y --nodocs         && \
    dnf install -y curl vim python3 && \
    dnf clean all                   && \
    rm -rf /var/cache/dnf

RUN mkdir -p /.config/
RUN cd ~
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    chown -R lumi:users /.config/
USER $NB_UID
EXPOSE 8080
ENTRYPOINT ["/bin/code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--cert", "false"]
