FROM illuminasaurus/python38-dl:20230315 as stage

FROM illuminasaurus/rstudio-eda:20230315

COPY --from=stage /opt/python/ /opt/python/

USER root

RUN dnf upgrade -y --nodocs	       && \
    dnf install -y libpng libpng-devel && \
    dnf clean all 	    	       && \
    rm -rf /var/cache/dnf

###################################################################################
# START CUDA UPDDATE
###################################################################################
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
RUN dnf upgrade -y --nodocs                                && \
    dnf install -y --nogpgcheck cuda-cudart-11-6-${NV_CUDA_CUDART_VERSION}    \
                                cuda-compat-11-6-${NV_CUDA_COMPAT_VERSION} && \
    ln -s cuda-11.6 /usr/local/cuda                        && \
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
ARG NV_CUDA_LIB_VERSION=11.6.2-1
ARG NV_NVTX_VERSION=11.6.124-1
ARG NV_LIBNPP_VERSION=11.6.3.124-1
ARG NV_LIBCUBLAS_VERSION=11.9.2.110-1
ARG NV_LIBNCCL_PACKAGE_VERSION=2.12.12-1
RUN dnf install -y --nogpgcheck cuda-libraries-11-6-${NV_CUDA_LIB_VERSION}        \
                                cuda-nvtx-11-6-${NV_NVTX_VERSION}                 \
                                libnpp-11-6-${NV_LIBNPP_VERSION}                  \
                                libcublas-11-6-${NV_LIBCUBLAS_VERSION}            \
                                libnccl-${NV_LIBNCCL_PACKAGE_VERSION}+cuda11.6 && \
    dnf clean all                                                              && \
    rm -rf /var/cache/dnf/
ARG NV_CUDNN_VERSION=8.4.1.50-1
RUN dnf install -yq --nogpgcheck libcudnn8-${NV_CUDNN_VERSION}.cuda11.6 && \
    dnf clean all                                                       && \
    rm -rf /var/cache/dnf/

ENV LD_LIBRARY_PATH /usr/local/cuda-11.6/targets/x86_64-linux/lib
RUN cp /usr/local/cuda-11.6/compat/libcuda.so.1 /usr/local/cuda-11.6/targets/x86_64-linux/lib/
########################################
# END CUDA UPDDATE
########################################

RUN R -e 'chooseCRANmirror(graphics = FALSE, ind = 92); install.packages(c("DMwR", "plyr", "reshape2", "GGally", "ggpubr", "ggridges", "RColorBrewer", "CausalImpact", "LogicReg", "prophet"), destdir = "/opt/R/4.2.2/lib/R/library/")'

USER 1001
EXPOSE 8787
ENTRYPOINT ["/tini", "-g", "--"]
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-user", "default"]
HEALTHCHECK --start-period=60s CMD rstudio-server status | grep -e "running"
