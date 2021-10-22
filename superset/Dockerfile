#NOTE: superset doesn't like python 3.8, one of the dependences has a python 3.6 requirement
FROM afcai2c/python36-ai:latest

ARG USERNAME
ARG PASSWORD

USER root

RUN yum update -y       && \
    yum clean all -y    && \
    yum install -y         \
        gcc                \
        gcc-c++            \
        libffi-devel       \
        python3-devel      \
        python3-pip        \
        python3-wheel      \
        openssl-devel      \
        cyrus-sasl-devel   \
        openldap-devel

RUN python3.6 -m pip install --upgrade   \
        setuptools                       \
        pip                           && \
    python3.6 -m pip install             \
        wheel                            \
        Pillow                           \
        dataclasses                      \
        gunicorn                         \
        psycopg2-binary                  \
        apache-superset

# Copy supserset config into python path
# All the parameters and default values defined in https://github.com/apache/incubator-superset/blob/master/superset/config.py can be altered in your local superset_config.py
COPY ./scripts/superset_config.py /usr/local/lib/python3.8/site-packages/

RUN superset db upgrade

RUN export FLASK_APP=superset

COPY ./scripts/init_superset.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/init_superset.sh

WORKDIR $HOME

ENTRYPOINT ["bash","/usr/local/bin/init_superset.sh"]

EXPOSE 8088

HEALTHCHECK --interval=10s --timeout=1s CMD curl --fail http://127.0.0.1:8088 || exit 1

# Example docker run:
# docker run -it --rm -p 8088:8088 -e USERNAME='username'' -e PASSWORD='password' afcai2c/superset:latest

