FROM afcai2c/jlab-dl:latest

USER root

WORKDIR /tmp/repo

RUN dnf upgrade -y --nodocs   && \
    dnf install -y mesa-libGL && \
    dnf clean all             && \
    rm -rf /var/cache/dnf

RUN python3.8 -m pip install   \
        # required for imutils
        opencv-python   \
        imutils         \
        pytesseract     \
        pytorchcv       \
        scikit-image

RUN . $VIRTUAL_ENV/bin/activate

RUN chmod g-s /usr/libexec/openssh/ssh-keysign                                                         && \
    rm -rf /tmp/repo                                                                                      \
           /opt/jupyter/venv/lib/python3.8/site-packages/bleach/_vendor/{Django-1.11.29.dist-info,django} \
           /opt/python/venv/lib/python3.8/site-packages/bleach/_vendor/{Django-1.11.29.dist-info,django}  \
           /opt/python/venv/lib/python3.8/site-packages/oslo_service/tests/                               \
           /usr/share/doc/perl-IO-Socket-SSL/certs/                                                       \
           /usr/share/doc/perl-IO-Socket-SSL/example/                                                     \
           /usr/share/doc/perl-Net-SSLeay/examples/
              
USER 1001

WORKDIR /home/jovyan

ENTRYPOINT ["tini", "-g", "--"]

CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1
