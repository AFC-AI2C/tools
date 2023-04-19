ARG STAGE_REGISTRY=illuminasaurus
ARG STAGE_IMAGE=python38-eda
ARG STAGE_TAG=20230418

ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=vs
ARG BASE_TAG=20230418

FROM ${STAGE_REGISTRY}/${STAGE_IMAGE}:${STAGE_TAG} AS py
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

RUN dnf upgrade -y --nodocs          && \
    dnf clean all                    && \
    rm -rf /var/cache/dnf

COPY --from=py /opt/python/venv/lib/python3.8/site-packages/ /usr/lib/python3.8/site-packages/

ENV PATH="${PATH:+${PATH}:}/opt/python/venv/:/usr/lib/python3.8/site-packages/"

RUN chmod -R 0750 /usr/lib/ 	    && \
    chmod -R 0750 /usr/local/bin/   && \
    chmod -R 0750 /usr/local/lib/   && \
    chmod -R 0750 /usr/local/lib64/ && \
    chown -R lumi /usr/lib/ 	    && \
    chown -R lumi /usr/local/lib/   && \
    chown -R lumi /usr/local/lib64/ && \
    chown -R lumi /usr/local/bin/

USER $NB_UID
EXPOSE 8080
ENTRYPOINT ["/bin/code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--cert", "false"]
