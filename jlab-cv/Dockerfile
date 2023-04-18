ARG STAGE_REGISTRY=illuminasaurus
ARG STAGE_IMAGE=python38-cv
ARG STAGE_TAG=20230418

ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=jlab
ARG BASE_TAG=20230418

FROM ${STAGE_REGISTRY}/${STAGE_IMAGE}:${STAGE_TAG} AS py
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

COPY --from=py /opt/python/venv/lib/python3.8/site-packages/ /opt/jupyter/venv/lib/python3.8/site-packages/

USER root

# makes the python packages accessible
ENV PATH="${PATH:+${PATH}:}/opt/python/venv/bin:/opt/jupyter/"

#Workaround for perl issue preventing yum upgrade
RUN dnf upgrade -y --nodocs  && \
    dnf install -y vim 		\
		   zip 		\
		   unzip 	\
		   net-tools 	\
		   # gcc is needed for prophet
		   gcc-c++ 	\
		   git 		\
		   gcc 	     && \
    dnf clean all	     && \
    rm -rf /var/cache/dnf

USER 1001
ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]
EXPOSE 8888
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
WORKDIR ~
