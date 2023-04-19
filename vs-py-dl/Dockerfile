ARG STAGE_REGISTRY=illuminasaurus
ARG STAGE_IMAGE=python38-dl
ARG STAGE_TAG=20230418

ARG BASE_REGISTRY=illuminasaurus
ARG BASE_IMAGE=vs-py-eda
ARG BASE_TAG=20230418

FROM ${STAGE_REGISTRY}/${STAGE_IMAGE}:${STAGE_TAG} AS py
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

COPY --from=py /opt/python/venv/lib/python3.8/site-packages/ /usr/lib/python3.8/site-packages/

USER root

# Makes the python packages accessible
ENV PATH="${PATH:+${PATH}:}/opt/python/venv/:/usr/lib/python3.8/site-packages/"

#Workaround for perl issue preventing yum upgrade
RUN dnf upgrade -y --nodocs && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

########################################
# START NVIDIA UPDDATE
########################################
# install cuda
ENV NVARCH x86_64
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.4 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"
ARG NV_CUDA_CUDART_VERSION=11.6.55-1
ARG NV_CUDA_COMPAT_VERSION=510.108.03-1

RUN dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel8/${NVARCH}/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -
RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

ARG CUDA_VERSION=11.6
## For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN dnf upgrade -y --nodocs                       && \
    dnf install -y --nogpgcheck cuda-cudart-11-6-${NV_CUDA_CUDART_VERSION}    \
                                cuda-compat-11-6-${NV_CUDA_COMPAT_VERSION} && \
    ln -s cuda-11.6 /usr/local/cuda               && \
    dnf clean all                                 && \
    rm -rf /var/cache/dnf

## nvidia-docker 1.0
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
ENV PATH="${PATH:+${PATH}:}/usr/local/nvidia/bin:/usr/local/cuda/bin"
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64
## nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

# install runtime (cudnn)
ARG NV_CUDA_LIB_VERSION=11.6.2-1
ARG NV_NVTX_VERSION=11.6.124-1
ARG NV_LIBNPP_VERSION=11.6.3.124-1
ARG NV_LIBCUBLAS_VERSION=11.9.2.110-1
ARG NV_LIBNCCL_VERSION=2.12.12-1
RUN dnf install -y --nogpgcheck cuda-libraries-11-6-${NV_CUDA_LIB_VERSION} \
                                cuda-nvtx-11-6-${NV_NVTX_VERSION}          \
                                libnpp-11-6-${NV_LIBNPP_VERSION}           \
                                libcublas-11-6-${NV_LIBCUBLAS_VERSION}     \
                                libnccl-${NV_LIBNCCL_VERSION}+cuda11.6  && \
    dnf clean all                                                       && \
    rm -rf /var/cache/dnf
ARG NV_CUDNN_VERSION=8.4.1.50-1
RUN dnf install -yq --nogpgcheck libcudnn8-${NV_CUDNN_VERSION}.cuda11.6 && \
    dnf clean all                                                       && \
    rm -rf /var/cache/dnf/

ENV LD_LIBRARY_PATH=/usr/local/cuda-11.6/targets/x86_64-linux/lib
RUN cp /usr/local/cuda-11.6/compat/libcuda.so.1 /usr/local/cuda-11.6/targets/x86_64-linux/lib/
########################################
# END NVIDIA UPDDATE
########################################

### removes vulnerable packages
RUN dnf remove -y kernel-headers \
                  binutils       \
                  openssl

### switches to default user to avoid running as root
USER $NB_UID
EXPOSE 8080
ENTRYPOINT ["/bin/code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none", "--cert", "false"] 
