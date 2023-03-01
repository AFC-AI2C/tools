FROM afcai2c/python38-eda:20230301il5 AS py

FROM afcai2c/jlab:20230301il5

COPY --from=py /opt/python/venv/lib/python3.8/site-packages/ /opt/jupyter/venv/lib/python3.8/site-packages/

USER root
WORKDIR /home/jovyan/
# Makes the python packages accessible
ENV PATH="/opt/python/venv/bin:/opt/jupyter/:$PATH"

#Workaround for perl issue preventing yum upgrade
RUN dnf upgrade -y --nodocs && \
    dnf install -y vim         \
        	   zip         \
        	   unzip       \
        	   net-tools   \
      		   # gcc is needed for prophet
        	   gcc-c++     \
        	   git      && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

### removes vulnerable packages
RUN dnf remove -y kernel-headers \
		  binutils 	 \
		  openssl

### switches back to jovyan to avoid container runs as root
USER 1001

ENTRYPOINT ["/tini", "-g", "--"]
CMD ["start-notebook.sh"]
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
WORKDIR ~
EXPOSE 8888
