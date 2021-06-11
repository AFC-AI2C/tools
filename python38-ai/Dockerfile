FROM afcai2c/python38

USER root

RUN yum upgrade -y      && \
    yum clean all -y    && \
    yum install -y         \
        vim                \
        zip                \
        unzip              \
        net-tools          \
        curl               \
        git                \
        gcc-c++

RUN mkdir -p /opt/python/repo
RUN chown -R 1001:users /opt/python

# dev
# COPY repo /opt/python/repo

# pipeline
COPY *.tar.gz /opt/python/repo
COPY *.whl /opt/python/repo

USER 1001

ENV VIRTUAL_ENV=/opt/python/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./scripts/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

#########################
# Compliance Mitigation #
#########################

USER root

# Removing unneeded vulnerable binaries
RUN rpm -e --nodeps   \
    binutils          \
    glibc-devel       \
    glibc-headers     \
    kernel-headers

# Removing identified secret
RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/certs/                 && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/               && \
    rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/               && \
    rm -rf /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem

# Modifying identified SUID files
RUN chmod g-s /usr/libexec/openssh/ssh-keysign

##########################
# Clean up install files #
##########################

RUN rm -rf /opt/python/repo   \
    rm /tmp/requirements.txt


USER 1001

WORKDIR $HOME

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1

#################
# local testing #
#################
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
# import prophet 
# import django
# import flask
