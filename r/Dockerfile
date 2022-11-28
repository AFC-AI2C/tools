# Default registry variables
ARG BASE_REGISTRY=redhat
ARG BASE_IMAGE=ubi8
ARG BASE_TAG=latest

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

ARG R_VERSION=4.2.2

ENV HOME=/home/default

RUN mkdir /repo ${HOME}

# pipeline
COPY R-${R_VERSION}-1-1.x86_64.rpm /repo/

COPY ./scripts /
RUN chmod +x fix-permissions

# import gpg key for r
COPY config/key.gpg ./
RUN rpm --import key.gpg
RUN rm -f ./*.gpg

# Install R and create simlinks to default system PATH for Rscripting and R repl
# using recommended approach as follows:  David Freeman 2021-10-15
#5:19 PM
#The short term fix is to use flags to ignore the signature or failing checksum. This pipeline succeeded and the Dockerfile can be copied in order #for build to succeed. The longer term solutions are to flag --nodigest type commands and require justifications, and to open tickets with the #upstream provider, to get them to change how they're signing the image.  https://repo1.dso.mil/dsop/opensource/r/r-base/-/blob/#77f7402073b1bcf7dd5039d6114a2adb5bc6631a/Dockerfile

RUN dnf upgrade -y --nodocs                                                                      && \
    dnf install -y less tk gcc bzip2-devel gcc-c++ gcc-gfortran libSM libXmu libXt                  \
                   libcurl-devel libicu-devel libtiff make openblas-threads pango pcre2-devel       \
                   tcl xz-devel zip zlib-devel cpp glibc-headers glibc-devel
RUN rpm -ivh /repo/R-${R_VERSION}-1-1.x86_64.rpm
RUN ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R                                             && \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript                                 && \
    dnf clean all                                                                                && \
    rm -rf /var/cache/dnf

# remove vulnerable packages installed by the RPM
# libcurl-7.61.1-14.el8_3.1.x86_64 is not removed as it is the same version as what is included in the base ubi8 image.

# every 10 seconds execute the R command specified to show 'healthy'
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

# Setup and run as the default user
RUN ./fix-permissions ${HOME} -P                        && \
    chmod -R 0750 /opt/R/${R_VERSION}/lib/R/             && \
    useradd -u 1001 -r -g 0 -d ${HOME} -s /bin/bash        \
    -c "Default Application User" default               && \
    chown -R 1001:0 ${HOME}                             && \
    chmod 0750 ${HOME}					&& \
    chown -R 1001 /opt/R/${R_VERSION}/lib/R/

ENV USER=default

USER 1001

WORKDIR ${HOME}
