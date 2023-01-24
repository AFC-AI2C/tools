ARG STAGE_REGISTRY=afcai2c
ARG STAGE_IMAGE=python38-eda
ARG STAGE_TAG=latest

ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=rstudio
ARG BASE_TAG=rebuild

FROM ${STAGE_REGISTRY}/${STAGE_IMAGE}:${STAGE_TAG} AS base
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

COPY --from=base /opt/python/ /opt/python/

USER root

RUN dnf upgrade -y --nodocs && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

RUN chown -R 10001 /var/lib/rstudio-server /var/run/rstudio-server /opt/R/ && \
    chmod -R g=u /var/lib/rstudio-server /var/run/rstudio-server /opt/R/   && \
    chmod -R g=u /etc/rstudio                                              && \
    chmod +x /var/run/rstudio-server

RUN R -e 'chooseCRANmirror(graphics=FALSE, ind=72); install.packages(destdir = "/opt/R/4.2.2/lib/R/library/", c("quarto", "numDeriv", "SQUAREM", "lava", "sys", "colorspace", "prodlim", "askpass", "farver", "labeling", "munsell", "RColorBrewer", "viridisLite", "fansi", "pkgconfig", "crayon", "utf8", "mime", "iterators", "gower", "ipred", "lubridate", "timeDate", "float", "RhpcBLASctl1", "RcppArmadillo", "curl", "openssl", "digest", "glue", "gtable", "isoband", "rlang", "scales", "tibble", "withr", "ellipsis", "generics", "lifecycle", "magrittr", "R6", "tidyselect", "vctrs", "pillar", "purrr", "cpp11", "evaluate", "highr", "markdown", "stringr", "yaml", "xfun", "foreach", "plyr", "ModelMetrics", "reshape2", "recipes", "pROC", "Rcpp", "rsparse", "stringi", "mlapi", "lgr", "cli", "httr", "jsonlite", "rjson", "ggplot", "data.table", "dplyr", "tidyr", "knitr", "caret", "text2vec", "osteR"))'

RUN echo 'LANG=en_US.UTF-8' >> /etc/locale.conf
ENV LC_ALL="en_US.utf8"
ENV LANGUAGE="en_US.utf8"

RUN chown -R 10001 /home/default/
RUN chmod -R 777 /home/default/

USER 10001
HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
EXPOSE 8787
ENTRYPOINT ["/tini", "-g", "--"]
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-user", "default"]
