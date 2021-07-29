ARG BASE_REGISTRY=registry1.dso.mil
ARG BASE_IMAGE=ironbank/opensource/r/r-studio
ARG BASE_TAG=4.0.3
FROM ${BASE_REGISTRY}/{BASE_IMAGE}:{BASE_TAG}

# # FROM registry.access.redhat.com/ubi8/ubi:latest
# #FROM afcai2c/r-base
# FROM afcai2c
# #FROM python-r-ai:latest
# FROM rstudio:27JulyTest 

USER root

RUN yum update -y &&                        \ 
    yum upgrade -y &&                       \
    yum clean all -y

RUN yum install -y curl

RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -

#THIS WILL BE ADDED TO THE HARDENING MANIFEST
COPY cuda.repo /etc/yum.repos.d/cuda.repo
COPY nvidia-ml.repo /etc/yum.repos.d/nvidia-ml.repo

ENV CUDA_VERSION 11.2.0

# For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN yum upgrade -y && yum install -y        \
    cuda-cudart-11-2-11.2.72-1              \
    cuda-compat-11-2                        \
    && ln -s cuda-11.2 /usr/local/cuda      \
    && yum clean all                        \
    && rm -rf /var/cache/yum/*

# nvidia-docker 1.0
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.2 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"

ENV NCCL_VERSION 2.8.4

RUN yum install -y                          \
    cuda-libraries-11-2-11.2.0-1            \
    cuda-nvtx-11-2-11.2.67-1                \
    libnpp-11-2-11.2.1.68-1                 \
    libcublas-11-2-11.3.1.68-1              \
    libnccl-2.8.4-1+cuda11.2                \
    && yum clean all                        \
    && rm -rf /var/cache/yum/*

RUN yum install -y                          \
    make                                    \
    cuda-command-line-tools-11-2-11.2.0-1   \
    cuda-libraries-devel-11-2-11.2.0-1      \
    cuda-minimal-build-11-2-11.2.0-1        \
    cuda-cudart-devel-11-2-11.2.72-1        \
    cuda-nvprof-11-2-11.2.67-1              \
    cuda-nvml-devel-11-2-11.2.67-1          \
    libcublas-devel-11-2-11.3.1.68-1        \
    libnpp-devel-11-2-11.2.1.68-1           \
    libnccl-devel-2.8.4-1+cuda11.2          \
    && yum clean all                        \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs


ENV CUDNN_VERSION 8.1.1.33
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"
RUN yum install -y                          \
    libcudnn8-${CUDNN_VERSION}-1.cuda11.2   \
    && yum clean all                        \
    && rm -rf /var/cache/yum/*


# These pacakges were removed from the-r-project to mitigate vulnerabilities, but are required for shiny and rmarkdown
RUN yum install -y                          \
    binutils                                \
    glibc-devel                             \
    glibc-headers                           \
    libX11                                  \
    kernel-headers


# Creates local R repository from the /tmp/repo directory
RUN R -e "tools::write_PACKAGES('/tmp/repo/')"

# Requested packages
RUN R -e "install.packages(c('tensorflow'), repos='http://cran.r-project.org', INSTALL_opts='--no-html')"

USER 1001 
RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install --upgrade pip
RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install --upgrade setuptools 
RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install tensorflow cuda cudnnenv keras ds2 fastai


RUN echo "PATH=/opt/python/venv/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/opt/python/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" > .Renviron
