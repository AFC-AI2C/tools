#ARG BASE_REGISTRY=registry1.dsop.io
#ARG BASE_IMAGE=ironbank/redhat/ubi/ubi8
#ARG BASE_TAG=8.3
#FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c/r-base:latest

USER root

RUN yum update -y && \ 
    yum upgrade -y && \
    yum clean all -y

# These pacakges were removed from the-r-project to mitigate vulnerabilities, but are required for shiny and rmarkdown
RUN yum install -y \
    binutils       \
    glibc-devel    \
    glibc-headers  \
    libX11         \
    kernel-headers

# Creates local R repository from the /tmp/repo directory
RUN R -e "tools::write_PACKAGES('/tmp/repo/')"

# Requested packages
RUN R -e "install.packages(c('tidyverse', 'shiny', 'plotly', 'shinydashboard', 'DT', 'rmarkdown', 'flexdashboard'), repos='http://cran.r-project.org', INSTALL_opts='--no-html')"

RUN yum -y install curl

WORKDIR /repo

RUN curl -LO https://download3.rstudio.org/centos7/x86_64/shiny-server-1.5.16.958-x86_64.rpm

RUN yum -y install --nogpgcheck shiny-server-1.5.16.958-x86_64.rpm && \
	rm -rf shiny-server-1.5.16.958-x86_64.rpm

RUN usermod shiny -g 0

RUN mkdir -p /var/log/shiny-server /var/lib/shiny-server/bookmarks \
	&& chown shiny:shiny /var/log/shiny-server /var/lib/shiny-server/bookmarks \
	&& chown shiny:shiny -R /srv/shiny-server \
	&& chmod 755 -R /srv/shiny-server \
	&& chown shiny:shiny -R /opt/shiny-server/samples/sample-apps /var/lib/shiny-server/bookmarks \
	&& chmod 755 -R /opt/shiny-server/samples/sample-apps

EXPOSE 3838

# shiny account is created when installing the shiny rpm
USER shiny

ENTRYPOINT [ "/usr/bin/shiny-server" ]