FROM afcai2c/python38-ai:latest

USER root 

COPY ./dash/scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER 1001

ENV HOME=/home/python
WORKDIR ~
RUN mkdir repo apps scripts

COPY ./dash/scripts/app.py $HOME/app.py

RUN pip install    \
        pip        \
        pandas     \
        dash

# cleanup downloaded packages
RUN rm -rf ~/repo

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

EXPOSE 8050

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
