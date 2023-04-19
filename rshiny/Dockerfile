ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=rbase
ARG BASE_TAG=20230418

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

#dnf remove -y epel-release
RUN dnf upgrade -y --nodocs	  && \
    dnf install -y binutils	     \
		   glibc-devel       \
		   glibc-headers     \
        	   kernel-headers && \
    dnf clean all 	    	  && \
    rm -rf /var/cache/dnf

# Requested packages
RUN R -e 'chooseCRANmirror(graphics = FALSE, ind = 90); install.packages(destdir = "/opt/R/4.2.3/lib/R/library/", c("tidyverse", "shiny", "plotly", "shinydashboard", "DT", "rmarkdown", "flexdashboard"))'

RUN curl -O https://download3.rstudio.org/centos7/x86_64/shiny-server-1.5.20.1002-x86_64.rpm && \
    dnf	install -y --nogpgcheck shiny-server-1.5.20.1002-x86_64.rpm   			     && \
    rm -f shiny-server-1.5.20.1002-x86_64.rpm

RUN mkdir -p /var/log/shiny-server /var/lib/shiny-server/bookmarks                            && \
	chown 1001 /var/log/shiny-server /var/lib/shiny-server/bookmarks                      && \
	chown 1001 -R /srv/shiny-server                                                       && \
	chmod 0750 -R /srv/shiny-server                                                        && \
	chown 1001 -R /opt/shiny-server/samples/sample-apps /var/lib/shiny-server/bookmarks   && \
	chmod 0750 -R /opt/shiny-server/samples/sample-apps

COPY ./scripts/shiny-customized.config /etc/shiny-server/shiny-server.conf

USER 1001

# shiny account is created when installing the shiny rpm
ENTRYPOINT [ "/usr/bin/shiny-server" ]
HEALTHCHECK --interval=10s --timeout=1s CMD curl localhost:3838 || exit 1
EXPOSE 3838
