FROM afcai2c/r-studio-ai:latest

USER root

ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8

RUN yum install -y      \
        binutils        \
        curl            \
        glibc-devel     \
        glibc-headers   \
        libcurl-devel   \
        libX11-common   \
        kernel-headers

RUN dnf update -y                  && \
    dnf install -qy --nogpgcheck      \
        glibc-langpack-en             \
        bind-utils                    \
        gettext                       \
        procps-ng                     \
        libaec                     && \
    dnf -y clean all

############################################################################################
# Install Base Supporting RPMS                                                             #
# sources:                                                                                 #
# https://github.com/CrunchyData/crunchy-containers/blob/master/build/base-ext/Dockerfile  #
# https://github.com/CrunchyData/crunchy-containers/blob/master/build/base/Dockerfile      #
############################################################################################

WORKDIR /opt

RUN curl -LO http://13.89.34.249/base-generic-supporting-rpms.tar.gz
RUN curl -LO http://13.89.34.249/base-epel-supporting-rpms.tar.gz
RUN curl -LO http://13.89.34.249/crunchy-postgres-rpms.tar.gz
RUN curl -LO http://13.89.34.249/crunchy-postgis-rpms.tar.gz

#COPY *tar.gz /opt
#RUN tar xf base-generic-supporting-rpms.tar.gz 
#RUN tar xf base-epel-supporting-rpms.tar.gz
#RUN dnf localinstall -qy base-generic-supporting-rpms/*.rpm 
#RUN dnf localinstall -qy base-epel-supporting-rpms/*.rpm 


############################################################################################
# Install Postgres-base Supporting RPMS                                                    #
# sources:                                                                                 #
# https://github.com/CrunchyData/crunchy-containers/blob/master/build/postgres/Dockerfile  #
############################################################################################

RUN tar xf crunchy-postgres-rpms.tar.gz 
RUN dnf localinstall -y --nogpgcheck crunchy-postgres-rpms/*.rpm 

###############################################################################################
# Install Postgis RPMS                                                                        #
# sources:                                                                                    #
# https://github.com/CrunchyData/crunchy-containers/blob/master/build/postgres-gis/Dockerfile #
###############################################################################################

RUN tar xf crunchy-postgis-rpms.tar.gz 
RUN dnf localinstall -y --nogpgcheck crunchy-postgis-rpms/*.rpm

USER 1001

EXPOSE 8787

ENTRYPOINT ["tini", "-g", "--"]

CMD ["rstudio-server", "start"]

HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
