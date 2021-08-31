FROM afcai2c/jlab-eda:latest

USER root

WORKDIR /tmp/repo

# Workaround for perl rpms preventing yum upgrade
RUN yum remove git -y  && \
    yum update -y -q   && \
    yum install -y -q     \
        gcc               \
        git               \
        make

COPY ./cuda/* /tmp/repo
COPY config/RPM-GPG-KEY-NVIDIA /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA

# Prepare cuda repo
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA 
RUN mkdir /etc/yum/repos.d
RUN curl -LO http://coeus-fileserver.centralus.cloudapp.azure.com/cuda_files.tar.gz
RUN tar -xzvf /tmp/repo/cuda_files.tar.gz -C /tmp/repo

# Install CUDA
ENV CUDA_VERSION 11.2.0

RUN yum upgrade -y                                          && \
    yum localinstall -y                                        \
        /tmp/repo/cuda-cudart-11-2-11.2.72-1.x86_64.rpm        \
        /tmp/repo/cuda-compat-11-2-460.91.03-1.x86_64.rpm   && \
    yum clean all                                           && \
    rm -rf /var/cache/yum/*

# Sets up the environment for cuda to find the appropriate folder locations. 
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.2 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"
ENV NCCL_VERSION 2.8.4

RUN yum localinstall -y                                       \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-nvrtc-11-2-11.2.67-1.x86_64.rpm            \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcublas-11-2-11.3.1.68-1.x86_64.rpm           \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcufft-11-2-10.4.0.72-1.x86_64.rpm            \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcurand-11-2-10.2.3.68-1.x86_64.rpm           \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcusolver-11-2-11.0.2.68-1.x86_64.rpm         \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcusparse-11-2-11.3.1.68-1.x86_64.rpm         \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libnpp-11-2-11.2.1.68-1.x86_64.rpm              \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libnvjpeg-11-2-11.3.1.68-1.x86_64.rpm

RUN yum localinstall -y                                       \
    /tmp/repo/cuda-libraries-11-2-11.2.0-1*.rpm               \
    /tmp/repo/cuda-nvtx-11-2-11.2.67-1*.rpm                   \
    /tmp/repo/libnccl-2.8.4-1+cuda11.2*.rpm                && \
    rm -rf /var/cache/yum/*

RUN yum localinstall -y                                       \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-cuobjdump-11-2-11.2.67-1.x86_64.rpm        \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-cuxxfilt-11-2-11.2.67-1.x86_64.rpm         \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-nvcc-11-2-11.2.67-1.x86_64.rpm             \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-nvprune-11-2-11.2.67-1.x86_64.rpm

RUN yum localinstall -y                                       \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-cupti-11-2-11.2.67-1.x86_64.rpm            \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-gdb-11-2-11.2.67-1.x86_64.rpm              \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-memcheck-11-2-11.2.67-1.x86_64.rpm         \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-nvdisasm-11-2-11.2.67-1.x86_64.rpm         \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-sanitizer-11-2-11.2.67-1.x86_64.rpm        \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-driver-devel-11-2-11.2.72-1.x86_64.rpm     \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-nvrtc-devel-11-2-11.2.67-1.x86_64.rpm      \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcufft-devel-11-2-10.4.0.72-1.x86_64.rpm      \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcurand-devel-11-2-10.2.3.68-1.x86_64.rpm     \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcusolver-devel-11-2-11.0.2.68-1.x86_64.rpm   \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcusparse-devel-11-2-11.3.1.68-1.x86_64.rpm   \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libnvjpeg-devel-11-2-11.3.1.68-1.x86_64.rpm     \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-compiler-11-2-11.2.0-1.x86_64.rpm

RUN yum localinstall -y                                       \
    /tmp/repo/cuda-command-line-tools-11-2-11.2.0-1*.rpm      \
    /tmp/repo/cuda-libraries-devel-11-2-11.2.0-1*.rpm         \
    /tmp/repo/cuda-minimal-build-11-2-11.2.0-1*.rpm           \
    /tmp/repo/cuda-cudart-devel-11-2-11.2.72-1*.rpm           \
    /tmp/repo/cuda-nvprof-11-2-11.2.67-1*.rpm                 \
    /tmp/repo/cuda-nvml-devel-11-2-11.2.67-1*.rpm             \
    /tmp/repo/libcublas-devel-11-2-11.3.1.68-1*.rpm           \
    /tmp/repo/libnpp-devel-11-2-11.2.1.68-1*.rpm              \
    /tmp/repo/libnccl-devel-2.8.4-1+cuda11.2*.rpm          && \
    yum clean all                                          && \
    rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs

RUN yum localinstall -y                                      \
    https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/libcudnn8-8.1.1.33-1.cuda11.2.x86_64.rpm          && \
    yum clean all                                         && \
    rm -rf /var/cache/yum/*


# Install python packages
RUN python3.8 -m pip install --upgrade  \
        pip                          && \
    python3.8 -m pip install            \
        wheel                           \
        pbr                             \
        tensorflow                      \ 
        ds2                             \
        torch                           \
        Keras                           \
        fastai                          \
        cudnnenv                        \
        gluon                        && \
    pip uninstall tf-nightly         && \
    pip install --upgrade --force-reinstall     \
        tensorflow                           && \
    python3.8 -m pip install --upgrade          \
        click                                   \
        SQLAlchemy
# uninstalling tf-nightly resolves keras.utils.generic_utils

RUN yum remove gcc -y  && \
    rm -rf /tmp/repo      \
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
              /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem \
    && chmod g-s /usr/libexec/openssh/ssh-keysign

RUN usermod -u 1002 python
RUN usermod -u 1001 jovyan
USER jovyan

RUN . $VIRTUAL_ENV/bin/activate

WORKDIR $HOME

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8888

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.6 -c 'print("up")' || exit 1


##################
# Testing Packages
    # import ds2
    # import tensorflow
    # import torch
    # import keras
    # import fastai
    # import cudnnenv
    # import gluon
