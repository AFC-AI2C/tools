FROM afcai2c/r-studio-eda:latest

USER root

RUN yum update -y &&                        \ 
    yum upgrade -y &&                       \
    yum clean all -y

RUN yum install -y curl

# These pacakges were removed from the-r-project to mitigate vulnerabilities, but are required for shiny and rmarkdown
RUN yum install -y                          \
    binutils                                \
    glibc-devel                             \
    glibc-headers                           \
    kernel-headers

########################################
# START ASE UPDDATE
########################################
# install cuda
ENV NVARCH x86_64
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.4 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"
ENV NV_CUDA_CUDART_VERSION 11.4.108-1
COPY ./cuda.repo-x86_64 /etc/yum.repos.d/cuda.repo

RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel8/${NVARCH}/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -
ENV CUDA_VERSION 11.4.1
## For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN yum upgrade -y && yum install -y \
    cuda-cudart-11-4-${NV_CUDA_CUDART_VERSION} \
    cuda-compat-11-4 \
    && ln -s cuda-11.4 /usr/local/cuda \
    && yum clean all \
    && rm -rf /var/cache/yum/*
## nvidia-docker 1.0
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
## nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# install runtime (cudnn)
ENV NV_CUDA_LIB_VERSION 11.4.1-1
ENV NV_NVTX_VERSION 11.4.100-1
ENV NV_LIBNPP_VERSION 11.4.0.90-1
ENV NV_LIBCUBLAS_VERSION 11.5.4.8-1
ENV NV_LIBNCCL_PACKAGE_NAME libnccl
ENV NV_LIBNCCL_PACKAGE_VERSION 2.10.3-1
ENV NV_LIBNCCL_VERSION 2.10.3
ENV NCCL_VERSION 2.10.3
ENV NV_LIBNCCL_PACKAGE ${NV_LIBNCCL_PACKAGE_NAME}-${NV_LIBNCCL_PACKAGE_VERSION}+cuda11.4
RUN yum install -y \
    cuda-libraries-11-4-${NV_CUDA_LIB_VERSION} \
    cuda-nvtx-11-4-${NV_NVTX_VERSION} \
    libnpp-11-4-${NV_LIBNPP_VERSION} \
    libcublas-11-4-${NV_LIBCUBLAS_VERSION} \
    ${NV_LIBNCCL_PACKAGE} \
    && yum clean all \
    && rm -rf /var/cache/yum/*
ENV NV_CUDNN_VERSION 8.2.2.26-1
ENV NV_CUDNN_PACKAGE libcudnn8-${NV_CUDNN_VERSION}.cuda11.4
RUN yum install -y ${NV_CUDNN_PACKAGE} \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LD_LIBRARY_PATH /usr/local/cuda-11.4/targets/x86_64-linux/lib
RUN cp /usr/local/cuda-11.4/compat/libcuda.so.1 /usr/local/cuda-11.4/targets/x86_64-linux/lib/
########################################
# END ASE UPDDATE
########################################

USER 1001

RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install --upgrade pip setuptools
RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install tensorflow keras ds2 fastai

USER root

# Required for R tensorflow
RUN yum install -y libpng libpng-devel

USER 1001

COPY ./scripts/ai-ml-packages.R .

RUN Rscript --no-save ai-ml-packages.R tensorflow

RUN echo "PATH=/opt/python/venv/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/opt/python/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" > .Renviron

EXPOSE 8787

ENTRYPOINT ["tini", "-g", "--"]

CMD ["rstudio-server", "start"]

HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
