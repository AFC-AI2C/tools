FROM afcai2c/python38-ai:latest AS multi-stage
FROM afcai2c/jupyterlab:latest

COPY --from=multi-stage /opt/python /opt/python

# Makes the python packages accessable
ENV PATH="/opt/python/venv/bin:$PATH"

USER root
#Workaround for perl issue preventing yum upgrade
RUN yum remove -y perl-threads
RUN yum upgrade -y        \
    && yum clean all -y   \
    && yum install -y     \
        vim               \
        zip               \
        unzip             \
        net-tools         \
        # gcc is needed for prophet
        gcc-c++           \
        git

# Needed to use packges from multi-stage build in Jupyterlab
RUN python3.8 -m pip install ipykernel

#########################
# Compliance Mitigation #
#########################

# Removing unneeded vulnerable binaries
RUN yum remove -y    \
    binutils         \
        # Medium - CVE-2021-20197, CVE-2021-20294, CVE-2021-3487
    glibc-devel      \
        # High   - CVE-2019-25013
        # Medium - CVE-2021-3326
        # Low    - CVE-2020-27618, CVE-2021-27645
    glibc-headers    \
        # High    - CVE-2019-25013
        # Medium - CVE-2021-3326
        # Low    - CVE-2020-27618, CVE-2021-27645
    #glibc-langpack-en \
    kernel-headers
        # High   - CVE-2020-12362, CVE-2020-36313
        # Medium - CVE-2019-20794, CVE-2020-0404, CVE-2020-0427, CVE-2020-0431, CVE-2020-10741, CVE-2020-12114, CVE-2020-12363, CVE-2020-12364, CVE-2020-13844, CVE-2020-14314, CVE-2020-14356, CVE-2020-14416, CVE-2020-15437, CVE-2020-15802, CVE-2020-24394, CVE-2020-24502, CVE-2020-24503, CVE-2020-24504, CVE-2020-25212, CVE-2020-25284, CVE-2020-25285, CVE-2020-25643, CVE-2020-25645, CVE-2020-25704, CVE-2020-26541, CVE-2020-27170, CVE-2020-27171, CVE-2020-27777, CVE-2020-27786, CVE-2020-27835, CVE-2020-28915, CVE-2020-28974, CVE-2020-29660, CVE-2020-35508, CVE-2020-36158, CVE-2020-4788, CVE-2020-8694, CVE-2021-0342, CVE-2021-20194, CVE-2021-20268, CVE-2021-28950, CVE-2021-28971, CVE-2021-28972, CVE-2021-29154, CVE-2021-29650, CVE-2021-3178, CVE-2021-3348, CVE-2021-3411, CVE-2021-3428, CVE-2021-3444
        # Low    - CVE-2019-20095, CVE-2020-11608, CVE-2020-14390, CVE-2020-35501, CVE-2021-20239


# Removing identified secret and SUID files
RUN rm -rf /usr/share/doc/perl-IO-Socket-SSL/certs/                   \
    && rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/              \
    && rm -rf /usr/share/doc/perl-IO-Socket-SSL/example/              \
    && rm -rf /usr/share/doc/perl-Net-SSLeay/examples/server_key.pem  \
    && rm -rf /opt/python/venv/lib/python3.8/site-packages/tornado/test/test.key \
    && chmod g-s /usr/libexec/openssh/ssh-keysign


USER jovyan

# Needed to use packges from multi-stage build in Jupyterlab
# A new kernel is displayed and available for use within JupyterLab
RUN python3.8 -m ipykernel install --name='AI_Packages' --user

WORKDIR $HOME

EXPOSE 8888

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1

