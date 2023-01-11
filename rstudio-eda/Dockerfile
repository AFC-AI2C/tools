ARG STAGE_REGISTRY=afcai2c
ARG STAGE_IMAGE=python38-eda
ARG STAGE_TAG=latest

ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=rstudio
ARG BASE_TAG=edits

FROM ${STAGE_REGISTRY}/${STAGE_IMAGE}:${STAGE_TAG} AS base
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY --from=base /usr/local/lib/ /usr/local/lib/
COPY --from=base /opt/python/ /opt/python/

USER root

RUN dnf upgrade -y --nodocs && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

COPY tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

RUN chown -R 10001 /var/lib/rstudio-server /var/run/rstudio-server /opt/R/ && \
    chmod -R g=u /var/lib/rstudio-server                                   && \
    chmod -R g=u /etc/rstudio                                              && \
    chmod +t /var/run/rstudio-server

RUN R -e 'chooseCRANmirror(graphics=FALSE, ind=100); install.packages(c("numDeriv", "SQUAREM", "lava", "sys", "colorspace", "prodlim", "askpass", "farver", "labeling", "munsell", "RColorBrewer", "viridisLite", "fansi", "pkgconfig", "crayon", "utf8", "mime", "iterators", "gower", "ipred", "lubridate", "timeDate", "float", "RhpcBLASctl1", "RcppArmadillo", "curl", "openssl", "digest", "glue", "gtable", "isoband", "rlang", "scales", "tibble", "withr", "ellipsis", "generics", "lifecycle", "magrittr", "R6", "tidyselect", "vctrs", "pillar", "purrr", "cpp11", "evaluate", "highr", "markdown", "stringr", "yaml", "xfun", "foreach", "plyr", "ModelMetrics", "reshape2", "recipes", "pROC", "Rcpp", "rsparse", "stringi", "mlapi", "lgr", "cli", "httr", "jsonlite", "rjson", "ggplot", "data.table", "dplyr", "tidyr", "knitr", "caret", "text2vec", "osteR"))'
RUN rm -f /opt/rstudio/RCurl/tests/dynSetReader.R                      \
          /opt/rstudio/openssl/tests/certigo/example-elliptic-sha1.key \
          /opt/rstudio/openssl/tests/keys/id_*                         \
          /opt/rstudio/gert/tests/testthat/key.pem                     \
          /opt/rstudio/gert/tests/testthat/ssh.key

RUN echo 'PATH="/opt/rstudio":$PATH' >> ~/.Renviron
RUN echo 'LANG=en_US.UTF-8' >> /etc/locale.conf

USER 10001
EXPOSE 8787
HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"

ENTRYPOINT ["tini", "-g", "--"]
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-user", "default"]
