FROM afcai2c/jlab-eda:latest

USER root
# Workaround for perl rpms preventing yum upgrade
RUN yum remove git -y
RUN yum update -y -q && \
    yum install -y -q \
    gcc \
    git

WORKDIR /tmp/repo

RUN python3.8 -m pip install --upgrade       \
        pip                               && \
    python3.8 -m pip install wheel        && \
    python3.8 -m pip install pbr          && \
    python3.8 -m pip install tensorflow   && \
    python3.8 -m pip install                 \
        ds2                                  \
        torch                                \
        Keras                                \
        fastai                               \
        cudnnenv                             \
        gluon                             && \
    pip uninstall tf-nightly              && \
    pip install tensorflow --upgrade --force-reinstall   && \
    python3.8 -m pip install --upgrade                      \
        click                                               \
        SQLAlchemy
    # uninstalling tf-nightly resolves keras.utils.generic_utils

# Removing identified secrets
RUN yum remove gcc -y   && \
    rm -rf /tmp/repo       \
           /opt/python/venv/lib/python3.8/site-packages/oslo_service/tests/ssl_cert/ca.key           \
           /opt/python/venv/lib/python3.8/site-packages/oslo_service/tests/ssl_cert/privatekey.key   \
           /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.enc           \
           /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.pem           \
           /usr/share/doc/perl-IO-Socket-SSL/certs/proxyca.pem              \
           /usr/share/doc/perl-IO-Socket-SSL/certs/server2-key.pem          \
           /usr/share/doc/perl-IO-Socket-SSL/certs/server-ecc-key.pem       \
           /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.enc           \
           /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.pem           \
           /usr/share/doc/perl-IO-Socket-SSL/certs/server-wildcard.pem      \
           /usr/share/doc/perl-IO-Socket-SSL/certs/sub-server.pem           \
           /usr/share/doc/perl-IO-Socket-SSL/example/simulate_proxy.pl      \
           /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem        && \
    chmod g-s /usr/libexec/openssh/ssh-keysign

USER jovyan

RUN . $VIRTUAL_ENV/bin/activate

WORKDIR $HOME

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1

