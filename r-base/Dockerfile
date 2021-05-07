FROM afcai2c/ubi8:latest

ARG R_VERSION=4.0.3

ENV HOME=/home/default

RUN mkdir /repo ${HOME}

# development building
WORKDIR /repo
RUN curl -O https://cdn.rstudio.com/r/centos-8/pkgs/R-${R_VERSION}-1-1.x86_64.rpm

COPY ./scripts /
RUN chmod +x /fix-permissions

# Install R and create simlinks to default system PATH for Rscripting and R repl
RUN yum update -y &&                                                 \
    yum install -y --nogpgcheck 					                 \
    less                                                             \
    /repo/R-${R_VERSION}-1-1.x86_64.rpm && 				             \
    ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R && 		     \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript &&  \
    yum clean all

# remove vulnerable packages installed by the RPM
# libcurl-7.61.1-14.el8_3.1.x86_64 is not removed as it is the same version as what is included in the base ubi8 image.
RUN rpm -e --nodeps \
    binutils        \
    curl 		    \
    glibc-devel 	\
    glibc-headers 	\
    libcurl-devel 	\
    libX11 		    \
    libX11-common 	\
    kernel-headers

# every 10 seconds execute the R command specified to show 'healthy'
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

# Setup and run as the default user
RUN /fix-permissions ${HOME} -P &&                   \
    chmod -R 771 /opt/R/${R_VERSION}/lib/R/ &&       \
    useradd -u 1001 -r -g 0 -d ${HOME} -s /bin/bash  \
    -c "Default Application User" default &&         \
    chown -R 1001:0 ${HOME}

ENV USER=default

USER 1001

WORKDIR ${HOME}
