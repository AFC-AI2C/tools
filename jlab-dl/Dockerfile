# Docker Hub Image Location
FROM afcai2c/jlab-eda:latest

USER root

RUN yum update -y -q && \
    yum install -y -q \
    gcc

RUN python3.6 -m pip install --upgrade \
        pip && \
    python3.6 -m pip install \
        ds2 \
        tensorflow \
        torch \
        Keras \
        fastai \
        cudnnenv \
        gluon

#USER jovyan
USER default

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1
