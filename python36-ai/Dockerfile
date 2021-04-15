ARG BASE_REGISTRY=registry1.dso.mil
ARG BASE_IMAGE=ironbank/redhat/python/python36
ARG BASE_TAG=3.6
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

#FROM photon:latest

# WORKDIR /tmp/repo
# COPY *.whl .
# COPY *.tar.gz .

# need to be root to install rpm files
USER root

RUN yum update -y && \
    yum upgrade -y && \
    yum clean all -y && \
    yum install -y \
        vim \
        zip \
        unzip \
        wget \
        net-tools\
        # gcc is needed for fbprophet
        gcc-c++ \
        git

# changing from root to default user 
USER default

RUN python3.6 -m pip install --upgrade  pip && \
    python3.6 -m pip install  \
        plotly \
        pandas \
        matplot \
        seaborn \
        numba \
        numpy \
        scipy \
        #import sklearn
        scikit-learn \
        tqdm \
        urllib3 \
        requests \
        #from bs4 import BeautifulSoup
        beautifulsoup4 \
        #from wordcloud import WordCloud
        wordcloud \
        statsmodels \
        fbprophet  \
        django \
        flask

USER root

# Allows Matplotlib to write to the directory. It is highly recommended to set the MPLCONFIGDIR environment variable to a writable directory, in particular to speed up the import of Matplotlib and to better support multiprocessing, otherwise it'll create a temporary config/cache direcotyr at /tmp/matplotlib-_ovd7aly.
RUN chown default /opt/app-root/src/

### Compliance Modification ###

# Upgrading to the version that was installed in pytho36 base
RUN yum upgrade -y \
    glibc-2.28-127.el8_3.2.x86_64 \
    glibc-common-2.28-127.el8_3.2.x86_64 \
    glibc-minimal-langpack-2.28-127.el8_3.2.x86_64

# Directed by Iron Bank to use previous version
# openssl is required for git
RUN yum install -y make && \
    rpm -e --nodeps openssl && \
    tar -xvzf openssl-1.1.1j.tar.gz && \
    cd openssl-1.1.1j && \
    ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl && \
    make && \
    make install && \
    mv /usr/local/openssl/bin/c_rehash /usr/bin && \
    mv /usr/local/openssl/bin/openssl /usr/bin && \
    rm -rf /usr/local/openssl && \
    rpm -e --nodeps make

# Upgrading click to patched version
RUN python3.6 -m pip uninstall click -y && \
    rm -f /tmp/repo/click-7.1.2-py2.py3-none-any.whl && \
    python3.6 -m pip install --no-index --find-links /tmp/repo click

# Removing identified secret and SUID files
RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/certs/ && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/ && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/ && \
    rm -rf /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem && \
    chmod g-s /usr/libexec/openssh/ssh-keysign

RUN yum remove -y \
    #Medium - No Description available [6Jan21]
    binutils \
    #High - The maximum impact of this vulnerability is a crash, and it relies on processing untrusted input in an uncommon encoding (EUC-KR). When this encoding is not used, the vulnerability can not be triggered.
            #Mitigation for this issue is either not available or the currently available options do not meet the Red Hat Product Security criteria comprising ease of use and deployment, applicability to widespread installation base or stability.
    glibc-devel \
    #High - The maximum impact of this vulnerability is a crash, and it relies on processing untrusted input in an uncommon encoding (EUC-KR). When this encoding is not used, the vulnerability can not be triggered.
            #Mitigation for this issue is either not available or the currently available options do not meet the Red Hat Product Security criteria comprising ease of use and deployment, applicability to widespread installation base or stability.
    glibc-headers \
    #High - The maximum impact of this vulnerability is a crash, and it relies on processing untrusted input in an uncommon encoding (EUC-KR). When this encoding is not used, the vulnerability can not be triggered.
    glibc-langpack-en \
    #High
    kernel-headers

WORKDIR $HOME

# RUN rm -rf /tmp/repo

USER default

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

# local testing
# import plotly
# import pandas
# import matplot
# import seaborn
# import numba
# import numpy
# import scipy
# import sklearn
# import tqdm
# import urllib3
# import requests
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import statsmodels
# import fbprophet 
# import django
# import flask
