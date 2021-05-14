FROM afcai2c/r-base:latest

USER root

RUN yum upgrade -y        \
    && yum clean all -y   \
    && yum install -y     \
        vim               \
        zip               \
        unzip             \
        wget              \
        net-tools         \
        gcc-c++           \
        git               \
        curl              \
        python38          \
        initscripts       \
        binutils          \
        glibc-devel       \
        glibc-headers     \
        libcurl-devel     \
        libX11 	          \
        libX11-common 	  \
        kernel-headers    \
        openssl-devel     \
        libxml2-devel  

USER default

RUN python3.8 -m pip install --user --upgrade  pip    && \
    python3.8 -m pip install --user                      \
        plotly           \
        pandas           \
        matplot          \
        seaborn          \
        numba            \
        numpy            \
        scipy            \
        scikit-learn     \
        tqdm             \
        urllib3          \
        requests         \
        beautifulsoup4   \
        wordcloud        \
        statsmodels      \
        django           \
        flask            
#       prophet

USER root

# R Studio Installation

WORKDIR /repo

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








USER default

# R Script to install pacakges and provides a stop error if in installation fails
COPY scripts/ai-ml-packages.R .


RUN Rscript --no-save ai-ml-packages.R broom
RUN Rscript --no-save ai-ml-packages.R C50
RUN Rscript --no-save ai-ml-packages.R cli
RUN Rscript --no-save ai-ml-packages.R DT
RUN Rscript --no-save ai-ml-packages.R ECharts2Shiny
RUN Rscript --no-save ai-ml-packages.R feather
RUN Rscript --no-save ai-ml-packages.R flexdashboard
RUN Rscript --no-save ai-ml-packages.R forcats
RUN Rscript --no-save ai-ml-packages.R foreign
RUN Rscript --no-save ai-ml-packages.R gt
RUN Rscript --no-save ai-ml-packages.R highcharter
RUN Rscript --no-save ai-ml-packages.R htmlwidgets
RUN Rscript --no-save ai-ml-packages.R httr
RUN Rscript --no-save ai-ml-packages.R kernlab
RUN Rscript --no-save ai-ml-packages.R kknn
RUN Rscript --no-save ai-ml-packages.R knitr
RUN Rscript --no-save ai-ml-packages.R lattice
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
RUN Rscript --no-save ai-ml-packages.R randomForest
RUN Rscript --no-save ai-ml-packages.R RCurl
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
RUN Rscript --no-save ai-ml-packages.R tidymodels
RUN Rscript --no-save ai-ml-packages.R tidytext
RUN Rscript --no-save ai-ml-packages.R xgboost
RUN Rscript --no-save ai-ml-packages.R readr
RUN Rscript --no-save ai-ml-packages.R readxl
RUN Rscript --no-save ai-ml-packages.R tidyverse
RUN Rscript --no-save ai-ml-packages.R timetk

# Copy in rpms
COPY *.rpm .


# Used npm to install xpm - not an R package
USER root
RUN yum install -y npm                 && \
    npm install --global xpm@latest


# reticulate R package
USER root
RUN yum install -y      \
        libpng-devel    \
        libpng
USER default
RUN Rscript --no-save ai-ml-packages.R reticulate 


# plumber R package
USER root
RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-devel-1.0.18-2.el8.x86_64.rpm   && \
    curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-1.0.18-2.el8.x86_64.rpm
RUN yum localinstall --nogpgcheck --skip-broken -y   \
        libsodium-devel-1.0.18-2.el8.x86_64.rpm      \
        libsodium-1.0.18-2.el8.x86_64.rpm
USER default
RUN Rscript --no-save ai-ml-packages.R plumber


# kableExtra R package
USER root
RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/i/ImageMagick-c++-devel-6.9.10.86-1.el8.x86_64.rpm   && \
    yum localinstall --nogpgcheck --skip-broken -y            \
        ImageMagick-c++-devel-6.9.10.86-1.el8.x86_64.rpm   && \
    yum install -y                                            \
        fontconfig-devel
USER default
RUN Rscript --no-save ai-ml-packages.R kableExtra  


# RJDBC R package
USER root
RUN yum install -y                     \
        java-1.8.0-openjdk             \
        java-1.8.0-openjdk-devel    && \
    R CMD javareconf
USER default
RUN Rscript --no-save ai-ml-packages.R RJDBC  


# leaflet package
RUN Rscript --no-save ai-ml-packages.R leaflet


# install pandoc
USER root
RUN curl -LO https://fossies.org/linux/www/pandoc-2.13-linux-amd64.tar.gz   && \
    tar xvzf pandoc-2.13-linux-amd64.tar.gz --strip-components 1 -C /usr/local


# devtools R package
USER root
RUN curl -LO http://mirror.centos.org/centos/8/PowerTools/x86_64/os/Packages/libgit2-devel-0.26.8-2.el8.i686.rpm    && \
    curl -LO http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/harfbuzz-devel-1.7.5-3.el8.x86_64.rpm   && \
    yum localinstall --nogpgcheck --skip-broken -y   \
        libgit2-devel-0.26.8-2.el8.i686.rpm          \
        harfbuzz-devel-1.7.5-3.el8.x86_64.rpm
USER default
RUN Rscript --no-save ai-ml-packages.R devtools











# Cleanup
USER root
RUN rm -rf /repo
USER default

ENTRYPOINT [ "rstudio-server","start" ]

HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

EXPOSE 8787


WORKDIR $HOME


