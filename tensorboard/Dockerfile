FROM afcai2c/jlab-dl:latest

COPY ./scripts/entrypoint.sh /entrypoint.sh

USER 1001

WORKDIR /home/jovyan

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]

EXPOSE 6006

HEALTHCHECK --interval=10s --timeout=1s CMD curl localhost:6006 || exit 1
