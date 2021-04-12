# IronBank Repo
#ARG BASE_REGISTRY=registry1.dso.mil
#ARG BASE_IMAGE=ironbank/opensource/python/python38
#ARG BASE_TAG=latest
#FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM high101bro/python38:latest

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
        # gcc is needed for prophet
        gcc-c++ \
        git

# the python38 image didn't have the default user account like the python36 image did
RUN useradd default

# changing from root to default user 
USER default

RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install \
    plotly \
    pandas \
    matplot \
    seaborn \
    numba \
    numpy \
    scipy \
    scikit-learn \
    tqdm \
    urllib3 \
    requests \
    beautifulsoup4 \
    wordcloud \
    statsmodels \
    django \
    flask \
    #prophet is the newer version of fbprophet
    prophet

USER default

CMD '/bin/bash'

WORKDIR $HOME

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1
