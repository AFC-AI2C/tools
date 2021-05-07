FROM afcai2c/r-base:latest

USER root

RUN yum update -y &&    \
    yum upgrade -y &&   \
    yum clean all -y && \
    yum install -y      \
        # Needed to start rstudio-server
        initscripts

# R Studio Installation

RUN yum install -y net-tools curl

WORKDIR /repo
#WORKDIR /tmp/repo 

#RUN ln -s /opt/R/4.0.3/lib/R /usr/lib/R

# Download R Studio rpm
RUN curl -LO https://download2.rstudio.org/server/centos8/x86_64/rstudio-server-rhel-1.4.1106-x86_64.rpm
#COPY rstudio-server-rhel-1.4.1106-x86_64.rpm .

# Obtaining the Public Key and validate 
# GnuPG key also located at as text: https://rstudio.com/code-signing/
#RUN gpg --keyserver keys.gnupg.net --recv-keys 3F32EE77E331692F
#RUN gpg --export --armor 3F32EE77E331692F > rstudio-signing.key
#RUN rpm --import rstudio-signing.key
#RUN rpm -K rstudio-server-rhel-1.4.1106-x86_64.rpm

# Install R Studio
RUN yum localinstall -y rstudio-server-rhel-1.4.1106-x86_64.rpm --nogpgcheck

# Verify Installation and write log
RUN rstudio-server verify-installation >> /tmp/rstudio-server.log

# Fixes permissions issue with sqlite3
RUN chown -R root:root /var/lib/rstudio-server
RUN chmod -R g=u /var/lib/rstudio-server

# Fixes issues with child images touching non-existing item 
RUN mkdir -p /var/lock/subsys/rstudio-server

#Disable RStudio Authentication
RUN cp /etc/rstudio/rserver.conf /etc/rstudio/disable_auth_rserver.conf
RUN echo "auth-none=1" >> /etc/rstudio/disable_auth_rserver.conf
    # If authentication is re-enabled, the free version of rstudio requires authentication using local linux credentials
    # the following creates an account with credentials to logon into rstudio
    #RUN useradd rstudio && \
    #    echo "rstudio:rstudio" | chpasswd

RUN mkdir /home/rstudio-server && \
    chown rstudio-server:rstudio-server /home/rstudio-server

# Cleanup
#RUN rm -rf /tmp/repo

ENTRYPOINT [ "rstudio-server","start" ]

HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

EXPOSE 8787

USER 1001



