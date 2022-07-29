FROM afcai2c/python-r-ai as base

FROM afcai2c/r-studio as final

USER root 

COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY --from=base /usr/local/lib/ /usr/local/lib/
COPY --from=base /opt/python/ /opt/python/
COPY --from=base /opt/R /opt/R

RUN dnf upgrade -y --nodocs && \
    dnf install -y openssl-libs curl openssl && \
    dnf clean all && \
    rm -rf /var/cache/dnf


RUN curl -LO https://github.com/krallin/tini/releases/download/v0.19.0/tini
RUN mv tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

# required to run rstudio hist commands, ex: hist(rnorm(100))
RUN dnf install -y libX11

USER 1001

EXPOSE 8787

ENTRYPOINT ["tini", "-g", "--"]

CMD ["rstudio-server", "start"]

HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
