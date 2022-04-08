FROM afcai2c/python38-ai as builder
FROM afcai2c/r-base as final

COPY --from=builder /opt/python /opt/python
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib

USER root

# Makes the python packages accessable
ENV PATH="/opt/python/venv/bin:$PATH"

#yum install -y --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN yum update -y       && \
    yum install -y         \
        vim                \
        zip                \
        unzip              \
        curl               \
        net-tools          \
        git                \
        # Needed to install various R packages
        gcc-c++            \
        binutils           \
        glibc-devel        \
        glibc-headers      \
        libcurl-devel      \
        libX11-common  	   \
        kernel-headers     \
        openssl-devel      \
        libxml2-devel

# Add repository, the UBI8 base image doesn't have this repository available and is not allowed within our CI/CD pipeline, thus needed here for the public version
ARG REDHAT_USERNAME='komnick'
ARG REDHAT_PASSWORD='muKZ!uNcw3CBaA7'
RUN subscription-manager register --auto-attach --username ${REDHAT_USERNAME} --password ${REDHAT_PASSWORD} && \
    subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms                            && \
    dnf install --nogpgcheck -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm      && \
    yum clean expire-cache && dnf update -y

# RUN dnf install epel-release epel-next-release

# R package dependencies within standard repos
# libsodium is required for the following packages
RUN dnf install -y \
        libsodium \
        libsodium-devel

# These rpms are required for the following packages
# The R_AIML_Deps.tar.gz contains multiple dependency rpms
    # dnf -y install --downloadonly --downloaddir=./ cairo cairo-devel fontconfig freetype freetype-devel harfbuzz-devel http-parser libgit2 libgit2-devel libXext-devel libXrender-devel pixman-devel protobuf-devel udunits2 gdal-libs gpsbabel ImageMagick-c++ ImageMagick-devel udunits2 cfitsio freexl gdal hdf5 netcdf ogdi proj xerces-c
RUN curl -LO http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/R_AIML_Deps.tar.gz     && \
    tar xvf R_AIML_Deps.tar.gz                                                                      && \
    yum localinstall -y ./repo/*.rpm --nogpgcheck

# R package dependencies within standard repos
RUN dnf install -y \
        #glib2 \
        #gdal-libs \
        #gdal \
        #gdtools \
        ImageMagick-c++-devel \
        udunits2-devel \
        fontconfig-devel              \
        #libpng                        \
        libpng-devel                  \
        libxslt-devel                 \
        java-1.8.0-openjdk            \
        java-1.8.0-openjdk-devel   && \
    yum clean packages

# Removes the subscription to the repositories added above
RUN subscription-manager unregister

# install pandoc
RUN curl -LO http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/pandoc-2.13-linux-amd64.tar.gz     && \
    tar xvzf pandoc-2.13-linux-amd64.tar.gz --strip-components 1 -C /usr/local                                  && \
# needed by RJDBC package
    R CMD javareconf

USER 1001

# R Script to install pacakges and provides a stop error if in installation fails
COPY ./python-r-ai/scripts/ai-ml-packages.R .

# R Packages can have a slow build time because they compile during installation
    # If you don't run R as root, you won't have permission to write packages into the default system-wide location and you will be prompted to create a personal library accessible by your userid. You can accept the personal library path chosen by R, or specify the library location by passing parameters to the install.packages function. For example, to create an R package repository in your home directory: R> install.packages("arules", lib="/home/username/Rpackages")
    # The ai-ml-packages.R script's purpose is to produce an error and stops the build if the R packages doesn't install
    # install.packages(c('broom','C50','cli','DT','ECharts2Shiny','feather','flexdashboard','forcats','foreign','gt','highcharter','htmlwidgets','httr','kernlab','kknn','knitr','lattice','lubridate','magrittr','Matrix','mlbench','nlme','nnet','openxlsx','packrat','parsnip','plotly','plotROC','randomForest','RCurl','rmarkdown','roxygen2','rvest','scales','shiny','shinydashboard','shinyWidgets','sparklyr','stringr','testthat','tidymodels','tidytext','xgboost','readr','readxl','tidyverse','timetk','devtools','ggiraph','flextable','kableExtra','leaflet','plumber','reticulate','rgdal','RJDBC','xpm'), dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest')
RUN Rscript --no-save ai-ml-packages.R \
    broom            \
    C50              \
    cli              \
    devtools         \
    DT               \
    ECharts2Shiny    \
    feather          \
    flexdashboard    \
    flextable        \
    forcats          \
    foreign          \
    ggiraph          \
    gt               \
    highcharter      \
    htmlwidgets      \
    httr             \
    kableExtra       \
    kernlab          \
    kknn             \
    knitr            \
    lattice          \
    leaflet          \
    lubridate        \
    magrittr         \
    Matrix           \
    mlbench          \
    nlme             \
    nnet             \
    openxlsx         \
    packrat          \
    parsnip          \
    plotly           \
    plotROC          \
    plumber          \
    randomForest     \
    RCurl            \
    readr            \
    readxl           \
    reticulate       \
    RJDBC            \
    rmarkdown        \
    roxygen2         \
    rvest            \
    scales           \
    shiny            \
    shinydashboard   \
    shinyWidgets     \
    sparklyr         \
    stringr          \
    testthat         \
    themis           \
    tidymodels       \
    tidytext         \
    tidyverse        \
    timetk           \
    xgboost

# Install reticulate miniconda packages, apparently not included when R installing reticulate
RUN R -e "reticulate::install_miniconda()"                          && \
#Sets path so R reticulate knows where python is located
    R -e "Sys.setenv(RETICULATE_PYTHON = '/usr/local/bin/python')"

# Used to check if path is set correctly
#R -e "reticulate::py_config()""

USER root

# Upgrading vulnerable binaries
RUN yum upgrade -y --skip-broken --allowerasing   \
        glibc            \
        glibc-common     \
        libdb            \
        libkadm5         \
        perl-libs        \
        perl-IO          \
        libwebp       && \
#Removing un-needed vulnerable binaries
    rpm -e --nodeps      \
        avahi-libs       \
        binutils         \
        cups-libs        \
        glibc-devel      \
        glibc-headers    \
        jasper-libs      \
        kernel-headers   \
        krb5-devel       \
        libcurl-devel    \
        libX11-common    \
        libxml2-devel    \
        perl-macros      \
        openssl-devel    \
        libtiff-devel    \
        jasper-devel     \
        glib2-devel      \
        libwebp-devel    \
        libX11-xcb       \
        libX11-devel     \
        pcre-utf16       \
        pcre-utf32       \
        pcre-cpp         \
        pcre-devel       \
        pcre2-devel   && \
# Removing secrets as identified in anchor scan
    rm -f /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.enc        \
          /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.pem        \
          /usr/share/doc/perl-IO-Socket-SSL/certs/proxyca.pem           \
          /usr/share/doc/perl-IO-Socket-SSL/certs/server2-key.pem       \
          /usr/share/doc/perl-IO-Socket-SSL/certs/server-ecc-key.pem    \
          /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.enc        \
          /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.pem        \
          /usr/share/doc/perl-IO-Socket-SSL/certs/server-wildcard.pem   \
          /usr/share/doc/perl-IO-Socket-SSL/certs/sub-server.pem        \
          /usr/share/doc/perl-IO-Socket-SSL/example/simulate_proxy.pl   \
          /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem

# Removing identified SUID files
RUN chmod g-s /usr/libexec/openssh/ssh-keysign          && \
# Removing vuln npm
    rm -rf /opt/R/4.0.3/lib/R/library/webshot/casperjs  && \
# Cleanup and Finalize #
    yum clean all                                       && \
    rm -rf ~/repo *.tar.gz *.R

USER 1001

WORKDIR ~

# every 10 seconds execute the R command specified to show 'healthy'
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

ENTRYPOINT [ "R" ]
