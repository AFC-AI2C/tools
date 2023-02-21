FROM afcai2c/python38-eda:20230209il5 AS multi-stage

FROM afcai2c/jlab:20230209il5

COPY --from=multi-stage /opt/python/ /opt/jupyter

USER root
# Makes the python packages accessable
ENV PATH="/opt/python/venv/bin:$PATH"
ENV PATH="/opt/jupyter/:$PATH"

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

WORKDIR ~
USER 1001
ENTRYPOINT ["/tini", "-g", "--"]
CMD ["start-notebook.sh"]
EXPOSE 8888
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1

