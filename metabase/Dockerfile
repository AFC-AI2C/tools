ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=openjdk11
ARG BASE_TAG=latest

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

ENV FC_LANG=en-US
ENV LC_CTYPE=en-US.UTF-8
ARG MB_EDITION=oss

RUN dnf upgrade -y --nodocs 	     && \
    dnf install -y ca-certificates 	\
		   dejavu-sans-fonts    \
		   fontconfig 	     && \
    dnf clean all		     && \
    rm -rf /var/cache/dnf

RUN useradd metabase && \
    usermod -u 1001 metabase

WORKDIR /etc/pki/ca-trust/source/anchors/

RUN chown metabase:metabase /etc/pki/ca-trust/source/anchors/ && \
    update-ca-trust force-enable			      && \
    update-ca-trust extract				      && \
    mkdir -p /plugins					      && \
    chmod a+rwx /plugins

WORKDIR /app/

COPY metabase.jar .
COPY scripts/entrypoint.sh .
COPY plugins/* /plugins

USER 1001
WORKDIR /home/metabase
EXPOSE 3000
ENTRYPOINT ["sh", "-c", "/app/entrypoint.sh"]
HEALTHCHECK CMD curl localhost:3000 || exit 1
