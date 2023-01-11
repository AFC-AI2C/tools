FROM afcai2c/rstudio-eda:rebuild

USER root

RUN dnf upgrade -y --nodocs       && \
    dnf install -y curl              \
                   binutils          \
                   glibc-devel       \
                   glibc-headers     \
                   kernel-headers && \
    dnf clean all                 && \
    rm -rf /var/cache/dnf/

########################################
# START ASE UPDDATE
########################################
# install cuda
ENV NVARCH x86_64
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.4 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"
ENV NV_CUDA_CUDART_VERSION 11.8.89-1
ENV NV_CUDA_COMPAT_VERSION 520.61.05-1
COPY ./cuda.repo-x86_64 /etc/yum.repos.d/cuda.repo

RUN dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel8/${NVARCH}/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -

ENV CUDA_VERSION 11.8
## For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN dnf upgrade -y --nodocs                                && \
    dnf install -y --nogpgcheck                               \
                cuda-cudart-11-8-${NV_CUDA_CUDART_VERSION}    \
                cuda-compat-11-8-${NV_CUDA_COMPAT_VERSION} && \
    ln -s cuda-11.8 /usr/local/cuda                        && \
    dnf clean all                                          && \
    rm -rf /var/cache/dnf/
## nvidia-docker 1.0
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
## nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# install runtime (cudnn)
ENV NV_CUDA_LIB_VERSION 11.8.0-1
ENV NV_NVTX_VERSION 11.8.86-1
ENV NV_LIBNPP_VERSION 11.8.0.86-1
ENV NV_LIBCUBLAS_VERSION 11.11.3.6-1
ENV NV_LIBNCCL_PACKAGE_NAME libnccl
ENV NV_LIBNCCL_PACKAGE_VERSION 2.15.5-1
ENV NV_LIBNCCL_VERSION 2.15.5-1
ENV NCCL_VERSION 2.15.5-1
ENV NV_LIBNCCL_PACKAGE ${NV_LIBNCCL_PACKAGE_NAME}-${NV_LIBNCCL_PACKAGE_VERSION}+cuda11.8
RUN dnf install -y --nogpgcheck cuda-libraries-11-8-${NV_CUDA_LIB_VERSION} \
                                cuda-nvtx-11-8-${NV_NVTX_VERSION}          \
                                libnpp-11-8-${NV_LIBNPP_VERSION}           \
                                libcublas-11-8-${NV_LIBCUBLAS_VERSION}     \
                                ${NV_LIBNCCL_PACKAGE}                   && \
    dnf clean all                                                       && \
    rm -rf /var/cache/dnf/
ENV NV_CUDNN_VERSION 8.7.0.84-1
ENV NV_CUDNN_PACKAGE libcudnn8-${NV_CUDNN_VERSION}.cuda11.8
RUN dnf install -yq --nogpgcheck ${NV_CUDNN_PACKAGE} && \
    dnf clean all                                    && \
    rm -rf /var/cache/dnf/

ENV LD_LIBRARY_PATH /usr/local/cuda-11.8/targets/x86_64-linux/lib
RUN cp /usr/local/cuda-11.8/compat/libcuda.so.1 /usr/local/cuda-11.8/targets/x86_64-linux/lib/
########################################
# END ASE UPDDATE
########################################

USER 10001

RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install --upgrade pip setuptools
RUN LD_LIBRARY_PATH=/usr/local/lib python3.8 -m pip install tensorflow keras ds2 fastai

USER root
RUN chown 10001 .Renviron
RUN chmod 0750 .Renviron

# Required for R tensorflow
RUN dnf install -y libpng libpng-devel

USER 10001

RUN echo "PATH=/opt/python/venv/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/opt/python/venv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" >> .Renviron

EXPOSE 8787
ENTRYPOINT ["tini", "-g", "--"]
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-user", "default"]
HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
