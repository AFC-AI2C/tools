FROM high101bro/python38:latest

USER root

RUN yum upgrade -y        \
    && yum clean all -y   \
    && yum install -y     \
        vim               \
        zip               \
        unzip             \
        wget              \
        net-tools         \
        # gcc is needed for prophet
        gcc-c++           \
        git


RUN mkdir -p /opt/python
RUN chown -R python3:users /opt/python


USER python3


ENV VIRTUAL_ENV=/opt/python/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . $VIRTUAL_ENV/bin/activate   && \
    pip install --upgrade  pip    && \
    pip install          \
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
        flask            \
        prophet


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
