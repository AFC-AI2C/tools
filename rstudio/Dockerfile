ARG BASE_REGISTRY=afcai2c
ARG BASE_IMAGE=rbase
ARG BASE_TAG=20230301il5

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

USER root

ENV RSTUDIO_VERSION=2022.12.0-353

RUN mkdir -p /tmp/rstudio/
COPY rstudio-server-rhel-${RSTUDIO_VERSION}-x86_64.rpm /tmp/rstudio/

COPY config/*.gpg ./
RUN rpm --import ./*.gpg
RUN rm -f ./*.gpg

RUN dnf upgrade -y --nodocs                                                                               && \
    dnf install -y glibc-langpack-en initscripts procps-ng openssl binutils libpq                            \
                   glibc-devel glibc-headers sqlite jq libpng-devel pcre krb5-libs                           \
                   cpp libgomp glibc-common glibc-langpack glibc libtiff libuuid yum-utils                   \
                   gcc libstdc++ libstdc++-devel expat gcc-c++ lua-libs ncurses-libs                         \
                   unzip zip cairo fontconfig freetype glib2 libcom_err libjpeg-turbo                        \
                   libsepol libX11 libxml2 pixman git glib2-devel psmisc java-devel                          \
                   kernel-headers libcurl-devel sqlite-devel libX11-common dnf-plugins-core                  \
                   libxml2-devel libtiff-devel libuuid-devel pcre-devel platform-python-pip                  \
                   net-tools openssl-devel fontconfig-devel freetype-devel java-17-openjdk-devel          && \
    rpm -ivh /tmp/rstudio/rstudio-server-rhel-${RSTUDIO_VERSION}-x86_64.rpm                               && \
    dnf remove xorg-x11-server-Xorg xorg-x11-server-common xorg-x11-server-utils xorg-x11-server-Xwayland && \
    dnf clean all                                                                                         && \
    rm -rf /var/cache/dnf

RUN mkdir -p /local/libs                                                            && \
    chown -R 1001 /var/lib/rstudio-server /var/run/rstudio-server /etc/rstudio      && \
    ln -s /usr/lib/rstudio-server/bin/rstudio-server /usr/local/bin/rstudio-server  && \
    chkconfig rstudio-server off

RUN echo "auth-none=1" >> /etc/rstudio/disable_auth_rserver.conf                            && \
    echo "server-daemonize=0" >> /etc/rstudio/rserver.conf                                  && \
    echo "[*]" > /etc/rstudio/logging.conf                                                  && \
    echo "log-level=warn" >> /etc/rstudio/logging.conf                                      && \
    echo "logger-type=stderr" >> /etc/rstudio/logging.conf                                  && \
    rm -rf /usr/bin/write /var/cache/dnf /tmp/* /local/libs/*                               && \
    update-crypto-policies --set

RUN chown -R 1001 /var/lib/rstudio-server && \
    chmod -R 0750 /var/lib/rstudio-server && \
    chown -R 1001 /etc/rstudio            && \
    chmod -R 0750 /etc/rstudio            && \
    chown -R 1001 /var/run/rstudio-server && \
    chmod -R 0750 /var/run/rstudio-server

# Clean up test keys and temporary files
RUN rm -rf /opt/r-packages-download/packrat/lib/x86_64-pc-linux-gnu/4.2.2/openssl/tests/keys/     \
           /opt/r-packages-download/packrat/lib/x86_64-pc-linux-gnu/4.2.2/openssl/tests/certigo/  \
           /usr/share/doc/perl-IO-Socket-SSL/certs/                                               \
           /usr/share/doc/perl-Net-SSLeay/examples/                                               \
           /usr/share/doc/perl-IO-Socket-SSL/example/                                             \
           /tmp/packrat/ /tmp/r-packages/ /tmp/rstudio/                                        && \
    rm -f  /usr/libexec/openssh/ssh-keysign

# NOTE: find command produces no results which leads to empty argument for "chmod a+t" portion
# RUN df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null | xargs chmod a+t

ENV LC_ALL="en_US.utf8"
ENV LANGUAGE="en_US.utf8"
ENV PATH="/usr/lib/rstudio-server/bin/rstudio-server:/usr/local/bin/rstudio-server:$PATH"
USER 1001
HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
EXPOSE 8787
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-user", "default"]
