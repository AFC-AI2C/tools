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

# R package dependencies within standard repos
# libsodium is required for the following packages
RUN yum localinstall --nogpgcheck -y              \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-1.0.18-2.el8.x86_64.rpm         \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-devel-1.0.18-2.el8.x86_64.rpm            

# These rpms are required for the following packages
# The R_AIML_Deps.tar.gz contains multiple dependency rpms
    # dnf -y install --downloadonly --downloaddir=./ cairo cairo-devel fontconfig freetype freetype-devel harfbuzz-devel http-parser libgit2 libgit2-devel libXext-devel libXrender-devel pixman-devel protobuf-devel udunits2 gdal-libs gpsbabel ImageMagick-c++ ImageMagick-devel udunits2 cfitsio freexl gdal hdf5 netcdf ogdi proj xerces-c
RUN curl -LO http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/R_AIML_Deps.tar.gz
RUN tar xvf R_AIML_Deps.tar.gz

RUN yum localinstall -y --nogpgcheck http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/glib2-2.56.4-156.el8.x86_64.rpm
#RUN yum localinstall -y ./repo/*.rpm --nogpgcheck

# R package dependencies within standard repos
RUN yum localinstall --nogpgcheck -y                       \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/g/gdal-libs-3.0.4-8.el8.x86_64.rpm                   \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/g/gdal-3.0.4-8.el8.x86_64.rpm                        \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/i/ImageMagick-c++-devel-6.9.10.86-1.el8.x86_64.rpm   \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/u/udunits2-devel-2.2.26-5.el8.x86_64.rpm

RUN yum install -y                    \
        fontconfig-devel              \
        libpng                        \
        libpng-devel                  \
        libxslt-devel                 \
        java-1.8.0-openjdk            \
        java-1.8.0-openjdk-devel   && \
    yum clean packages

# install pandoc
RUN curl -LO http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/pandoc-2.13-linux-amd64.tar.gz
RUN tar xvzf pandoc-2.13-linux-amd64.tar.gz --strip-components 1 -C /usr/local

# needed by RJDBC package
RUN R CMD javareconf

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
    forcats          
RUN Rscript --no-save ai-ml-packages.R \
    foreign          \
    ggiraph          \
    gt               \
    highcharter      \
    htmlwidgets      \
    httr             \
    kableExtra       \
    kernlab          \
    kknn             \
    knitr            
RUN Rscript --no-save ai-ml-packages.R \
    lattice          \
    leaflet          \
    lubridate        \
    magrittr         \
    Matrix           \
    mlbench          \
    nlme             \
    nnet             \
    openxlsx         \
    packrat
RUN Rscript --no-save ai-ml-packages.R \
    parsnip          \
    plotly           \
    plotROC          \
    plumber          \
    randomForest     \
    RCurl            \
    readr            \
    readxl           \
    reticulate       \
    RJDBC
RUN Rscript --no-save ai-ml-packages.R \
    rmarkdown        \
    roxygen2         \
    rvest            \
    scales           \
    shiny            \
    shinydashboard   \
    shinyWidgets     \
    sparklyr         \
    stringr          \
    testthat
RUN Rscript --no-save ai-ml-packages.R \
    themis           \
    tidymodels       \
    tidytext         \
    tidyverse        \
    timetk           \
    xgboost

#Sets path so R reticulate knows where python is located
RUN R -e "Sys.setenv(RETICULATE_PYTHON = '/usr/local/bin/python')"

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
        libwebp

#Removing un-needed vulnerable binaries
RUN rpm -e --nodeps      \
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
        pcre2-devel

# Removing secrets as identified in anchor scan
RUN rm -f /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.enc        \
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
RUN chmod g-s /usr/libexec/openssh/ssh-keysign

# Removing vuln npm
RUN rm -rf /opt/R/4.0.3/lib/R/library/webshot/casperjs

# Cleanup and Finalize #
RUN yum clean all   && \
    rm -rf ~/repo *.tar.gz *.R

USER 1001

WORKDIR ~

# every 10 seconds execute the R command specified to show 'healthy'
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

ENTRYPOINT [ "R" ]
