FROM afcai2c/python38-ai as builder
FROM afcai2c/r-base

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

RUN curl -LO http://13.89.34.249/R_AIML_Deps.tar.gz 
# COPY *.tar.gz /tmp/repo/
# COPY *.rpm .

# R package dependencies within standard repos
# libsodium is required for the following packages
RUN yum localinstall --nogpgcheck -y              \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-1.0.18-2.el8.x86_64.rpm         \
        https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-devel-1.0.18-2.el8.x86_64.rpm            

# These rpms are required for the following packages
# The R_AIML_Deps.tar.gz contains multiple dependency rpms
    # dnf -y install --downloadonly --downloaddir=./ cairo cairo-devel fontconfig freetype freetype-devel harfbuzz-devel http-parser libgit2 libgit2-devel libXext-devel libXrender-devel pixman-devel protobuf-devel udunits2 gdal-libs gpsbabel ImageMagick-c++ ImageMagick-devel udunits2 cfitsio freexl gdal hdf5 netcdf ogdi proj xerces-c
RUN mkdir -p /tmp/repo/R_AIML_Deps                                     
RUN tar xvf R_AIML_Deps.tar.gz -C /tmp/repo/R_AIML_Deps   
RUN yum localinstall --nogpgcheck -y /tmp/repo/R_AIML_Deps/repo/*.rpm

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

# Creates local R repository from the /tmp/repo directory
#RUN R -e "tools::write_PACKAGES('/tmp/repo/')"

# install pandoc
RUN curl -LO http://13.89.34.249/pandoc-2.13-linux-amd64.tar.gz
RUN tar xvzf pandoc-2.13-linux-amd64.tar.gz --strip-components 1 -C /usr/local

# needed by RJDBC package
RUN R CMD javareconf

USER 1001

# R Script to install pacakges and provides a stop error if in installation fails
COPY scripts/ai-ml-packages.R .

# R Packages can have a slow build time because they compile during installation
    # If you don't run R as root, you won't have permission to write packages into the default system-wide location and you will be prompted to create a personal library accessible by your userid. You can accept the personal library path chosen by R, or specify the library location by passing parameters to the install.packages function. For example, to create an R package repository in your home directory: R> install.packages("arules", lib="/home/username/Rpackages")
    # The ai-ml-packages.R script's purpose is to produce an error and stops the build if the R packages doesn't install
    # install.packages(c('broom','C50','cli','DT','ECharts2Shiny','feather','flexdashboard','forcats','foreign','gt','highcharter','htmlwidgets','httr','kernlab','kknn','knitr','lattice','lubridate','magrittr','Matrix','mlbench','nlme','nnet','openxlsx','packrat','parsnip','plotly','plotROC','randomForest','RCurl','rmarkdown','roxygen2','rvest','scales','shiny','shinydashboard','shinyWidgets','sparklyr','stringr','testthat','tidymodels','tidytext','xgboost','readr','readxl','tidyverse','timetk','devtools','ggiraph','flextable','kableExtra','leaflet','plumber','reticulate','rgdal','RJDBC','xpm'), dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest')
RUN Rscript --no-save ai-ml-packages.R broom
RUN Rscript --no-save ai-ml-packages.R C50
RUN Rscript --no-save ai-ml-packages.R cli
RUN Rscript --no-save ai-ml-packages.R devtools
RUN Rscript --no-save ai-ml-packages.R DT
RUN Rscript --no-save ai-ml-packages.R ECharts2Shiny
RUN Rscript --no-save ai-ml-packages.R feather
RUN Rscript --no-save ai-ml-packages.R flexdashboard
RUN Rscript --no-save ai-ml-packages.R flextable
RUN Rscript --no-save ai-ml-packages.R forcats
RUN Rscript --no-save ai-ml-packages.R foreign
RUN Rscript --no-save ai-ml-packages.R ggiraph
RUN Rscript --no-save ai-ml-packages.R gt
RUN Rscript --no-save ai-ml-packages.R highcharter
RUN Rscript --no-save ai-ml-packages.R htmlwidgets
RUN Rscript --no-save ai-ml-packages.R httr
RUN Rscript --no-save ai-ml-packages.R kableExtra  
RUN Rscript --no-save ai-ml-packages.R kernlab
RUN Rscript --no-save ai-ml-packages.R kknn
RUN Rscript --no-save ai-ml-packages.R knitr
RUN Rscript --no-save ai-ml-packages.R lattice
RUN Rscript --no-save ai-ml-packages.R leaflet
RUN Rscript --no-save ai-ml-packages.R lubridate
RUN Rscript --no-save ai-ml-packages.R magrittr
RUN Rscript --no-save ai-ml-packages.R Matrix
RUN Rscript --no-save ai-ml-packages.R mlbench
RUN Rscript --no-save ai-ml-packages.R nlme
RUN Rscript --no-save ai-ml-packages.R nnet
RUN Rscript --no-save ai-ml-packages.R openxlsx
RUN Rscript --no-save ai-ml-packages.R packrat
RUN Rscript --no-save ai-ml-packages.R parsnip
RUN Rscript --no-save ai-ml-packages.R plotly
RUN Rscript --no-save ai-ml-packages.R plotROC
RUN Rscript --no-save ai-ml-packages.R plumber
RUN Rscript --no-save ai-ml-packages.R randomForest
RUN Rscript --no-save ai-ml-packages.R RCurl
RUN Rscript --no-save ai-ml-packages.R readr
RUN Rscript --no-save ai-ml-packages.R readxl
RUN Rscript --no-save ai-ml-packages.R reticulate 
RUN Rscript --no-save ai-ml-packages.R RJDBC  
RUN Rscript --no-save ai-ml-packages.R rmarkdown
RUN Rscript --no-save ai-ml-packages.R roxygen2
RUN Rscript --no-save ai-ml-packages.R rvest
RUN Rscript --no-save ai-ml-packages.R scales
RUN Rscript --no-save ai-ml-packages.R shiny
RUN Rscript --no-save ai-ml-packages.R shinydashboard
RUN Rscript --no-save ai-ml-packages.R shinyWidgets
RUN Rscript --no-save ai-ml-packages.R sparklyr
RUN Rscript --no-save ai-ml-packages.R stringr
RUN Rscript --no-save ai-ml-packages.R testthat
RUN Rscript --no-save ai-ml-packages.R themis
RUN Rscript --no-save ai-ml-packages.R tidymodels
RUN Rscript --no-save ai-ml-packages.R tidytext
RUN Rscript --no-save ai-ml-packages.R tidyverse
RUN Rscript --no-save ai-ml-packages.R timetk
RUN Rscript --no-save ai-ml-packages.R xgboost


#COPY scripts/web_install.R .
#RUN Rscript --no-save web_install.R rgdal

# RUN  yum install -y --skip-broken \
#         npm
# USER 1001
# # Used npm to install xpm - not an R package
# RUN npm install --global xpm@latest

#########################
# Compliance Mitigation #
#########################
USER root

# NOTE: perl's upgrade is broken, so using --nobest
# https://bugzilla.redhat.com/show_bug.cgi?id=1963049

# Upgrading vulnerable binaries
RUN yum upgrade -y --skip-broken --allowerasing --nobest   \
        glibc            \
        glibc-common     \
        libdb            \
        libkadm5         \
        perl-libs        \
        perl-IO

# Removing un-needed vulnerable binaries
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
        pcre-cpp         \
        pcre-devel       \
        libwebp-devel

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

########################
# Cleanup and Finalize #
########################

RUN rm -rf /tmp/repo/

USER 1001

WORKDIR $HOME

# every 10 seconds execute the R command specified to show 'healthy'
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

#################
# Test Commands #
#################
# vim --version
# zip --help
# unzip --help
# curl www.google.com
# netstat
# git clone https://www.github.com/high101bro/Docker.git
# pandoc --version
# xpm --version

# python3.8 -c 'import sqlite3'
# python3.8 -c 'import plotly'
# python3.8 -c 'import pandas'
# python3.8 -c 'import matplot'
# python3.8 -c 'import seaborn'
# python3.8 -c 'import numba'
# python3.8 -c 'import numpy'
# python3.8 -c 'import scipy'
# python3.8 -c 'import sklearn'
# python3.8 -c 'import tqdm'
# python3.8 -c 'import urllib3'
# python3.8 -c 'import requests'
# python3.8 -c 'from bs4 import BeautifulSoup'
# python3.8 -c 'from wordcloud import WordCloud'
# python3.8 -c 'import statsmodels'
# python3.8 -c 'import prophet'
# python3.8 -c 'import django'
# python3.8 -c 'import flask'

# R -e "plot(c(1,2,3),c(1,2,3))"
# R -e "library('broom')"
# R -e "library('C50')"
# R -e "library('cli')"
# R -e "library('DT')"
# R -e "library('ECharts2Shiny')"
# R -e "library('feather')"
# R -e "library('flexdashboard')"
# R -e "library('forcats')"
# R -e "library('foreign')"
# R -e "library('gt')"
# R -e "library('htmlwidgets')"
# R -e "library('kernlab')"
# R -e "library('kknn')"
# R -e "library('knitr')"
# R -e "library('lattice')"
# R -e "library('lubridate')"
# R -e "library('magrittr')"
# R -e "library('Matrix')"
# R -e "library('mlbench')"
# R -e "library('nlme')"
# R -e "library('nnet')"
# R -e "library('openxlsx')"
# R -e "library('packrat')"
# R -e "library('parsnip')"
# R -e "library('randomForest')"
# R -e "library('RCurl')"
# R -e "library('readr')"
# R -e "library('readxl')"
# R -e "library('rmarkdown')"
# R -e "library('scales')"
# R -e "library('shiny')"
# R -e "library('shinydashboard')"
# R -e "library('shinyWidgets')"
# R -e "library('stringr')"
# R -e "library('testthat')"
# R -e "library('tidymodels')"
# R -e "library('tidytext')"
# R -e "library('tinytex')"
# R -e "library('xgboost')"
# R -e "library('devtools')"
# R -e "library('highcharter')"
# R -e "library('httr')"
# R -e "library('kableExtra')"
# R -e "library('leaflet')"
# R -e "library('plotly')"
# R -e "library('plotROC')"
# R -e "library('plumber')"
# R -e "library('reticulate')"
# R -e "library('RJDBC')"
# R -e "library('roxygen2')"
# R -e "library('rvest')"
# R -e "library('sparklyr')"
# R -e "library('tidyverse')"
# R -e "library('timetk')"
# R -e "library('flextable')"
# R -e "library('ggiraph')"
# R -e "library('rgdal')"
