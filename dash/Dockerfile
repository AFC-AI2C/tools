FROM illuminasaurus/python38-eda:20230315

USER root 

COPY ./scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV HOME=/home/python

WORKDIR /home/python
RUN mkdir repo apps scripts

COPY ./scripts/app.py $HOME/app.py
RUN dnf remove -y kernel-headers

USER 1001

HEALTHCHECK CMD curl --fail http://127.0.0.1:8050 || exit 1

EXPOSE 8050

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]
