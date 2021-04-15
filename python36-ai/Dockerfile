# ARG BASE_REGISTRY=registry1.dso.mil
# ARG BASE_IMAGE=ironbank/redhat/python/python36
# ARG BASE_TAG=3.6
# FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

FROM afcai2c/python36:latest

USER root

RUN yum update -y &&    \
    yum upgrade -y &&   \
    yum clean all -y && \
    yum install -y      \
        vim             \
        zip             \
        unzip           \
        wget            \
        net-tools       \
        gcc-c++         \
        git

USER default

RUN python3.6 -m pip install --upgrade  pip && \
    python3.6 -m pip install                   \
        plotly                                 \
        pandas                                 \
        matplot                                \
        seaborn                                \
        numba                                  \
        numpy                                  \
        scipy                                  \
        scikit-learn                           \
        tqdm                                   \
        urllib3                                \
        requests                               \
        beautifulsoup4                         \
        wordcloud                              \
        statsmodels                            \
        fbprophet                              \
        django                                 \
        flask

USER root

RUN chown default /opt/app-root/src/

# RUN yum upgrade -y \
#     glibc-2.28-127.el8_3.2.x86_64 \
#     glibc-common-2.28-127.el8_3.2.x86_64 \
#     glibc-minimal-langpack-2.28-127.el8_3.2.x86_64

# RUN yum install -y make && \
#     rpm -e --nodeps openssl && \
#     tar -xvzf openssl-1.1.1j.tar.gz && \
#     cd openssl-1.1.1j && \
#     ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl && \
#     make && \
#     make install && \
#     mv /usr/local/openssl/bin/c_rehash /usr/bin && \
#     mv /usr/local/openssl/bin/openssl /usr/bin && \
#     rm -rf /usr/local/openssl && \
#     rpm -e --nodeps make

# RUN python3.6 -m pip uninstall click -y && \
#     rm -f /tmp/repo/click-7.1.2-py2.py3-none-any.whl && \
#     python3.6 -m pip install --no-index --find-links /tmp/repo click

# RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/certs/ && \
#     rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/ && \
#     rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/ && \
#     rm -rf /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem && \
#     chmod g-s /usr/libexec/openssh/ssh-keysign

# RUN yum remove -y     \
#     binutils          \
#     glibc-devel       \
#     glibc-headers     \
#     glibc-langpack-en \
#     kernel-headers

WORKDIR $HOME

USER default

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1