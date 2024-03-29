FROM afcai2c/python38

USER root

RUN dnf upgrade -y      && \
    dnf install -y         \
        vim                \
        zip                \
        unzip              \
        net-tools          \
        curl               \
        git                \
        gcc-c++         && \
    dnf clean all -y    && \
    rm -rf /var/cache/dnf

RUN mkdir -p /opt/python/repo
RUN chown -R 1001:users /opt/python

USER 1001

ENV VIRTUAL_ENV=/opt/python/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install          \
        pip              \
        wheel            \
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
        prophet          \
        dvc              \
        mlflow           \
        alibi            \
        alibi-detect     \
        boto3

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

# Mitigate django v1.1.14 packaged w/pypi bleach
RUN rm -rf /opt/python/venv/lib/python3.8/site-packages/bleach/_vendor/django                    \
           /opt/python/venv/lib/python3.8/site-packages/bleach/_vendor/Django-1.11.29.dist-info

# Modifying identified SUID files
RUN chmod g-s /usr/libexec/openssh/ssh-keysign

RUN rm -rf /opt/python/repo

USER 1001

WORKDIR ~

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1

