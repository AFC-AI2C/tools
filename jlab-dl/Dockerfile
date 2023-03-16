FROM illuminasaurus/python38-dl:20230315 AS py

FROM illuminasaurus/jlab:20230315

COPY --from=py /opt/python/venv/lib/python3.8/site-packages/ /opt/jupyter/venv/lib/python3.8/site-packages/

USER root
WORKDIR /home/jovyan/
# Makes the python packages accessible
ENV PATH="/opt/python/venv/bin:/opt/jupyter/:$PATH"

#Workaround for perl issue preventing yum upgrade
RUN dnf upgrade -y --nodocs && \
    dnf install -y vim         \
                   zip         \
                   unzip       \
                   net-tools   \
                   # gcc is needed for prophet
                   gcc-c++     \
                   git      && \
    dnf clean all           && \
    rm -rf /var/cache/dnf

########################################
# START NVIDIA UPDDATE
########################################
# install cuda
ENV NVARCH x86_64
ENV NVIDIA_REQUIRE_CUDA "cuda>=11.4 brand=tesla,driver>=418,driver<419 brand=tesla,driver>=440,driver<441 driver>=450"
ENV NV_CUDA_CUDART_VERSION 11.8.89-1
COPY cuda.repo-x86_64 /etc/yum.repos.d/cuda.repo

RUN dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/rhel8/${NVARCH}/7fa2af80.pub | sed '/^Version/d' > /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    echo "$NVIDIA_GPGKEY_SUM  /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA" | sha256sum -c --strict -
ENV CUDA_VERSION 11.8
## For libraries in the cuda-compat-* package: https://docs.nvidia.com/cuda/eula/index.html#attachment-a
RUN dnf upgrade -y --nodocs                       && \
    dnf install -y --nogpgcheck                      \
       cuda-cudart-11-8-${NV_CUDA_CUDART_VERSION}    \
       cuda-compat-11-8                           && \
    ln -s cuda-11.8 /usr/local/cuda               && \
    dnf clean all

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
    				cuda-nvtx-11-8-${NV_NVTX_VERSION} 	   \
    				libnpp-11-8-${NV_LIBNPP_VERSION} 	   \
    				libcublas-11-8-${NV_LIBCUBLAS_VERSION}     \
    				${NV_LIBNCCL_PACKAGE} 			&& \
    dnf clean all
ENV NV_CUDNN_VERSION 8.6.0.163-1
ENV NV_CUDNN_PACKAGE libcudnn8-${NV_CUDNN_VERSION}.cuda11.8
RUN dnf install -yq --nogpgcheck ${NV_CUDNN_PACKAGE} && \
    dnf clean all				     && \
    rm -rf /var/cache/dnf/

ENV LD_LIBRARY_PATH /usr/local/cuda-11.4/targets/x86_64-linux/lib
RUN cp /usr/local/cuda-11.8/compat/libcuda.so.1 /usr/local/cuda-11.8/targets/x86_64-linux/lib/
########################################
# END NVIDIA UPDDATE
########################################

### removes vulnerable packages
RUN dnf remove -y kernel-headers \
                  binutils       \
                  openssl

### switches back to jovyan to avoid container runs as root
USER 1001

ENTRYPOINT ["/tini", "-g", "--"]
CMD ["start-notebook.sh"]
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
WORKDIR ~
EXPOSE 8888

