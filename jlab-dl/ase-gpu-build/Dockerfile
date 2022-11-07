FROM localhost/jlab-eda:latest

USER root
RUN dnf upgrade -y && \
    dnf install -y --nodocs gcc git make && \
    dnf clean all && \
    rm -rf /var/cache/dnf

RUN mkdir -p /tmp/repo/

COPY ./config/keys/ /etc/pki/rpm-gpg/

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-NVIDIA && \
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8 

### STEP 0 - Determine CUDA version on ASE
    # https://192.168.20.185/AzureStackEdge/#SoftwareUpdate
        # CUDA version: 11.7
        # cuda  = 11.7
        # cudnn = 8.4.1.50
        # Not compatible: 8.4.0.24,8.6.0.163

### NVIDIA CUDA/Cudnn installation
    # https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#prerequisites
    # Check out the NVIDIA cuDNN Support Matrix
        # https://docs.nvidia.com/deeplearning/cudnn/support-matrix/index.html

### STEP 2.1.1. Installing NVIDIA Graphics Drivers
    # https://www.nvidia.com/Download/index.aspx?lang=en-us
    #..... Umm.... skipped this for now, the underlying ASE hardware should abstarct this away from us


### STEP 2.1.2 Installing the CUDA Toolkit for Linux
# https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#installcuda
    # Search for the specific cuda toolkit for the OS used
        # https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
            # Install gcc
            # https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-that-gcc-is-installed
RUN dnf install -y gcc

# https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#redhat8-installation-prepare
    # wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
COPY ./epel-release-latest-8.noarch.rpm /tmp/repo
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/epel-release-latest-8.noarch.rpm
# Enables Code Ready Builder
RUN /usr/bin/crb enable
RUN subscription-manager register --username='komnick' --password='muKZ!uNcw3CBaA7' --auto-attach --force
RUN subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
RUN subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms
RUN subscription-manager repos --enable=rhel-8-for-x86_64-baseos-rpms
RUN subscription-manager repos --enable=codeready-builder-for-rhel-8-x86_64-rpms 
            # ERROR:
            # subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms
        # RUN rpm --erase gpg-pubkey-7fa2af80*


            # The kernel headers and development packages for the currently running kernel can be installed with: 
                # dnf install kernel-devel error:
                # No match for argument: kernel-devel-5.4.0-1061-fips
                # No match for argument: kernel-headers-5.4.0-1061-fips
                # Error: Unable to find a match: kernel-devel-5.4.0-1061-fips kernel-headers-5.4.0-1061-fips
# RUN dnf install kernel-devel-$(uname -r) kernel-headers-$(uname -r)
    # Downlaod the CUDA Tookkit 11.8
    # https://developer.nvidia.com/cuda-downloads
        # https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=RHEL&target_version=8&target_type=rpm_local
        # ... not using 11.8
    # Download the CUDA Toolkit 11.70
    # https://developer.nvidia.com/cuda-11-7-1-download-archive
        # https://developer.nvidia.com/cuda-11-7-1-download-archive?target_os=Linux&target_arch=x86_64&Distribution=RHEL&target_version=8&target_type=rpm_local
        # Download this file and copy it into the container
            # wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda-repo-rhel8-11-7-local-11.7.1_515.65.01-1.x86_64.rpm
COPY ./cuda-repo-rhel8-11-7-local-11.7.1_515.65.01-1.x86_64.rpm /tmp/repo
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/cuda-repo-rhel8-11-7-local-11.7.1_515.65.01-1.x86_64.rpm
RUN dnf clean all
RUN dnf -y module install \
        nvidia-driver:latest-dkms
COPY ./cuda /tmp/repo/cuda
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/cuda/*.rpm

# # ### STEP 2.1.3 Installing zlib${cuda}
# # # https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-zlib-linux
RUN yum install -y zlib


# # ### STEP 2.2. Downloading cuDNN for Linux
# # # https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#download
# #     # https://developer.nvidia.com/rdp/cudnn-download
# #         # Select cuDNN version for CUDA 11.x
# #         # Download this file and copy it into the container
# #             # wget https://developer.nvidia.com/compute/cudnn/secure/8.6.0/local_installers/11.8/cudnn-local-repo-rhel8-${cudnn}-1.0-1.x86_64.rpm
COPY ./cudnn-local-repo-rhel8-8.4.1.50-1.0-1.x86_64.rpm /tmp/repo
COPY ./libcudnn8-8.4.1.50-1.cuda10.2.x86_64.rpm /tmp/repo
# # ### Section 2.3.3 RPM Local Installation
# #     # https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#installlinux-rpm
# # # Enable the local repository
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/cudnn-local-repo-rhel8-8.4.1.50-1.0-1.x86_64.rpm && \
    # Refresh the repository metadata
    dnf -y clean all
# Install the runtime library
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/libcudnn8-8.4.1.50-1.cuda10.2.x86_64.rpm
RUN dnf install libcudnn -y
# ENV LD_LIBRARY_PATH=/usr/local/cuda-11/lib64:$LD_LIBRARY_PATH                                                              │1 Record inserted successfully into drones table
# ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
COPY ./cudnn-local-repo-rhel8-8.6.0.163-1.0-1.x86_64.rpm /tmp/repo
RUN rpm --install --noplugins --nodigest --nosignature \
        /tmp/repo/cudnn-local-repo-rhel8-8.6.0.163-1.0-1.x86_64.rpm && \
    # Refresh the repository metadata
    dnf -y clean all


# These libraries do not exist as of 20221101
    # Install the developer library
    # RUN yum install -y libcudnn8=8.4.1.50-1.11.7
    # Install the code samples andthe cuDNN library documentation
    # RUN yum install -y libcudnn8-devel=8.4.1.50-1.11.7



# Install python packages
COPY requirements.txt /opt/python/

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
# ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64
ENV LD_LIBRARY_PATH /opt/python/venv/lib/python3.8/site-packages/nvidia/cuda_runtime/lib
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs

# Install python packages
COPY requirements.txt /opt/python/

# first install wheel to avoid pip trying to use packages' setup.py
RUN pip install wheel && \
    pip install --upgrade pip
RUN pip uninstall tf-nightly && \
    pip install --upgrade \
        click \
        SQLAlchemy
RUN pip install -r /opt/python/requirements.txt

# https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-pycuda
RUN pip install 'pycuda<2021.1'
#RUN pip install --upgrade --force-reinstall tensorflow

# 2022-11-04 22:36:30.220182: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
# To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
# 2022-11-04 22:36:31.426399: E tensorflow/stream_executor/cuda/cuda_blas.cc:2981] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
# 2022-11-04 22:36:35.715239: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/python/venv/lib/python3.8/site-packages/nvidia/cuda_runtime/lib
# 2022-11-04 22:36:35.716013: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7: cannot open shared object file: No such file or directory; LD_LIBRARY_PATH: /opt/python/venv/lib/python3.8/site-packages/nvidia/cuda_runtime/lib
# 2022-11-04 22:36:35.716092: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.















# Clean up
RUN dnf clean all -y && \
    yum clean all -y && \
    rm -rf /tmp/repo


USER jovyan
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
    # import gluoncv
