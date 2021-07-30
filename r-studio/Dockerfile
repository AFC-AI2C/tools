FROM registry1.dso.mil/ironbank/aiml/python/python-r-ai as base

FROM registry1.dso.mil/ironbank/opensource/r/r-studio as final

USER root 

COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY --from=base /usr/local/lib/ /usr/local/lib/
COPY --from=base /opt/python/ /opt/python/

RUN yum install -y curl
RUN curl -LO https://github.com/krallin/tini/releases/download/v0.19.0/tini
RUN mv tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

USER 1001

EXPOSE 8787

ENTRYPOINT ["tini", "-g", "--"]

CMD ["rstudio-server", "start"]

HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
