# ARG BASE_REGISTRY=registry1.dsop.io
# ARG BASE_IMAGE=ironbank/redhat/python/python36
# ARG BASE_TAG=3.6
# FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c/python36-ai:latest

WORKDIR /opt/app-root
RUN mkdir repo apps scripts default

COPY scripts/app.py /opt/app-root/default/app.py 

RUN python3.6 -m pip install \
    pip                      \
    pandas                   \
    dash

# cleanup downloaded packages
# RUN rm -rf /opt/app-root/repo
# remove IB flagged 'secrets'
# RUN rm /opt/app-root/lib/python3.6/site-packages/future/backports/test/badcert.pem     \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/badkey.pem         \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/keycert2.pem       \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/keycert.passwd.pem \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/keycert.pem        \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/ssl_key.passwd.pem \
#     /opt/app-root/lib/python3.6/site-packages/future/backports/test/ssl_key.pem

# only use root to copy in and chmod the entrypoint
USER root 
COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

# switch to default user to run the container
USER default

# port for default app.py
EXPOSE 8050

# the way to use this is to mount in an app.py to /opt/app-root/apps/app.py in the container
ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]