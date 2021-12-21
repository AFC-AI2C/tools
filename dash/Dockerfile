FROM afcai2c/python38-ai:latest

USER root 

COPY ./dash/scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER 1001

ENV HOME=/home/python

WORKDIR /home/jovyan

COPY ./dash/scripts/app.py ~/app.py

RUN pip install    \
        pip        \
        pandas     \
        dash

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

EXPOSE 8050

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
