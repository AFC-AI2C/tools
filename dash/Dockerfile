FROM afcai2c/python38-ai:latest

USER root 

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER 1001

ENV HOME=/home/python
WORKDIR $HOME
RUN mkdir repo apps scripts

COPY scripts/app.py $HOME/app.py

RUN pip install    \
        pip        \
        pandas     \
        dash       \
        gunicorn

# Removing identified secrets
RUN rm /opt/python/venv/lib/python3.8/site-packages/future/backports/test/*.pem

# cleanup downloaded packages
RUN rm -rf $HOME/repo

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

EXPOSE 8050

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
