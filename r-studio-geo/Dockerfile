# FROM afcai2c/r-studio-eda:latest
FROM afcai2c/r-studio-eda:latest

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

# Add repository, the UBI8 base image doesn't have this repository available and is not allowed within our CI/CD pipeline, thus needed here for the public version
ARG REDHAT_USERNAME
ARG REDHAT_PASSWORD
RUN subscription-manager register --auto-attach --username ${REDHAT_USERNAME} --password ${REDHAT_PASSWORD} && \
    subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms                            && \
    dnf install --nogpgcheck -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm      && \
    yum clean expire-cache && dnf update -y

RUN dnf -y install --nogpgcheck https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
RUN dnf -y module disable postgresql
RUN dnf -y install epel-release


RUN dnf install -y \
    postgresql \
    postgis

USER 1001

# COPY ./r-studio-geo/scripts/ai-ml-packages.R .
COPY ./scripts/ai-ml-packages.R .

# RUN Rscript -e "install.packages('leafem', dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest');"
# RUN Rscript -e "install.packages('leafem', dependencies=TRUE);"
  
# RUN Rscript --no-save ai-ml-packages.R \
#     satellite
# RUN Rscript --no-save ai-ml-packages.R \
#     leafpop

#RUN Rscript -e "install.packages('rgdal', dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest');"
RUN Rscript --no-save ai-ml-packages.R \
    rgdal 
# RUN Rscript --no-save ai-ml-packages.R \
    # rasterio 
# RUN Rscript --no-save ai-ml-packages.R \
    # geopy 
# RUN Rscript --no-save ai-ml-packages.R \
    # sarpy
# RUN Rscript --no-save ai-ml-packages.R \
#     maps
# RUN Rscript --no-save ai-ml-packages.R \
#     leaflet
# RUN Rscript --no-save ai-ml-packages.R \
#     sf
# RUN Rscript --no-save ai-ml-packages.R \
#     sp
# RUN Rscript --no-save ai-ml-packages.R \
#     raster
# RUN Rscript --no-save ai-ml-packages.R \
#     stars
# RUN Rscript --no-save ai-ml-packages.R \
#     maptools
# RUN Rscript --no-save ai-ml-packages.R \
#     spatstat
# RUN Rscript --no-save ai-ml-packages.R \
#     inimisc
# RUN Rscript --no-save ai-ml-packages.R \
#     rgdal
# RUN Rscript --no-save ai-ml-packages.R \
#     ggmap
# RUN Rscript --no-save ai-ml-packages.R \
#     rwordmap
# RUN Rscript --no-save ai-ml-packages.R \
#     Rgooglemaps
# RUN Rscript --no-save ai-ml-packages.R \
#     rnaturalearth
# RUN Rscript --no-save ai-ml-packages.R \
#     terra
# RUN Rscript --no-save ai-ml-packages.R \
#     ggplot2
# RUN Rscript --no-save ai-ml-packages.R \
#     munging

# # Removes the subscription to the repositories added above
# RUN subscription-manager unregister

# USER 1001

# EXPOSE 8787

# ENTRYPOINT ["tini", "-g", "--"]

# CMD ["rstudio-server", "start"]

# HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
