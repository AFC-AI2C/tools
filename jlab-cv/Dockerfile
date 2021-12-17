FROM afcai2c/jlab-dl:latest

USER root

WORKDIR /tmp/repo

RUN python3.8 -m pip install   \
        # required for imutils
        opencv-python   \
        imutils         \
        pytesseract     \
        pytorchcv       \
        scikit-image
RUN yum install -y mesa-libGL

RUN . $VIRTUAL_ENV/bin/activate

RUN chmod g-s /usr/libexec/openssh/ssh-keysign \
    && rm -rf /tmp/repo \
              /opt/jupyter/venv/lib/python3.8/site-packages/bleach/_vendor/{Django-1.11.29.dist-info,django} \
              /opt/python/venv/lib/python3.8/site-packages/bleach/_vendor/{Django-1.11.29.dist-info,django} \
              /opt/python/venv/lib/python3.8/site-packages/oslo_service/tests/ssl_cert/ca.key \
              /opt/python/venv/lib/python3.8/site-packages/oslo_service/tests/ssl_cert/privatekey.key \
              /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.enc \
              /usr/share/doc/perl-IO-Socket-SSL/certs/client-key.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/proxyca.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/server2-key.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/server-ecc-key.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.enc \
              /usr/share/doc/perl-IO-Socket-SSL/certs/server-key.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/server-wildcard.pem \
              /usr/share/doc/perl-IO-Socket-SSL/certs/sub-server.pem \
              /usr/share/doc/perl-IO-Socket-SSL/example/simulate_proxy.pl \
              /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem 

USER 1001

WORKDIR ~

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1
