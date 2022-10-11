from redhat/ubi8:latest

USER root

ARG NB_USER="lumi"
ARG NB_UID="1000"
ARG NB_GID="100"

RUN dnf upgrade -y --nodocs && \
    dnf install -y curl vim && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

#RUN mkdir ~/config/
#RUN mkdir -p /.config/
RUN cd ~
RUN curl -fsSL https://code-server.dev/install.sh | sh
#RUN touch ~/config/config.yaml
#ENV SET="auth: none\nbind-addr: 0.0.0.0:8080\ncert: false"
#RUN echo -e $SET >> ~/config/config.yaml

#ENV PATH="/usr/bin/code-server:/bin/code-server":$PATH
#ENV bind="0.0.0.0:8080"
#ENV auth="none"
#ENV cert="false"

#USER $NB_UID
EXPOSE 8080
ENTRYPOINT ["/bin/code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--cert", "false"] 
#CMD [code-server --bind-addr $bind --auth $auth --cert $cert]
#ENTRYPOINT ["code-server --bind-addr 0.0.0.0:8080 --auth none --cert false"]
