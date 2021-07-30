FROM afcai2c/python-r-ai:latest

USER root

RUN yum update -y         && \ 
    yum clean all -y      && \
    yum install -y           \
        binutils             \
        glibc-devel          \
        glibc-headers        \
        kernel-headers

RUN mkdir -p /tmp/repo/
COPY *.tar.gz /tmp/repo/

# Creates local R repository from the /tmp/repo directory
RUN R -e "tools::write_PACKAGES('/tmp/repo/')"

USER 1001

# R Script to install pacakges and provides a stop error if in installation fails
COPY ./scripts/web_install.R .

# Requested packages
#RUN R -e "install.packages(c('tidyverse', 'shiny', 'plotly', 'shinydashboard', 'DT', 'rmarkdown', 'flexdashboard'), dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest')"
#RUN R -e "install.packages(c('tidyverse', 'shiny', 'plotly', 'shinydashboard', 'DT', 'rmarkdown', 'flexdashboard'), dependencies=TRUE, repos=NULL, recursive=TRUE, contriburl='file://tmp/repo/')"
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

COPY ./scripts/shiny-customized.config /etc/shiny-server/shiny-server.conf

#RUN usermod -aG shiny default

USER 1001
#USER shiny

# shiny account is created when installing the shiny rpm
#USER shiny
ENTRYPOINT [ "/usr/bin/shiny-server" ]

HEALTHCHECK --interval=10s --timeout=1s CMD curl localhost:3838 || exit 1

EXPOSE 3838
