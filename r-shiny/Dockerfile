FROM afcai2c/python-r-ai:latest

USER root

#dnf remove -y epel-release
RUN dnf install -y           \
        binutils             \
        glibc-devel          \
        glibc-headers        \
        kernel-headers

USER 1001

# R Script to install pacakges and provides a stop error if in installation fails
#COPY ./r-shiny/scripts/web_install.R .
COPY scripts/web_install.R .

# Requested packages
RUN Rscript --no-save web_install.R   \
    tidyverse        \
    shiny            \
    plotly           \
    shinydashboard   \
    DT               \
    rmarkdown        \
    flexdashboard


RUN curl -O https://download3.rstudio.org/centos7/x86_64/shiny-server-1.5.16.958-x86_64.rpm

USER root

RUN yum install -y --nogpgcheck shiny-server-1.5.16.958-x86_64.rpm   && \
	rm -f shiny-server-1.5.16.958-x86_64.rpm

RUN mkdir -p /var/log/shiny-server /var/lib/shiny-server/bookmarks                        && \
	chown 1001 /var/log/shiny-server /var/lib/shiny-server/bookmarks                      && \
	chown 1001 -R /srv/shiny-server                                                       && \
	chmod 755 -R /srv/shiny-server                                                        && \
	chown 1001 -R /opt/shiny-server/samples/sample-apps /var/lib/shiny-server/bookmarks   && \
	chmod 755 -R /opt/shiny-server/samples/sample-apps

#COPY ./r-shiny/scripts/shiny-customized.config /etc/shiny-server/shiny-server.conf
COPY scripts/shiny-customized.config /etc/shiny-server/shiny-server.conf

USER 1001

# shiny account is created when installing the shiny rpm
ENTRYPOINT [ "/usr/bin/shiny-server" ]

HEALTHCHECK --interval=10s --timeout=1s CMD curl localhost:3838 || exit 1

EXPOSE 3838
