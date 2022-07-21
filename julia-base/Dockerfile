FROM redhat/ubi8

ARG USER="joules"
ARG UID="1000"
ARG GID="100"

# Update base packages
RUN dnf upgrade -y --nodocs && \
    dnf clean all && \
    rm -rf /var/cache/dnf

# Install julia
RUN mkdir /julia/ && cd ./
RUN curl https://julialang-s3.julialang.org/bin/linux/x64/1.7/julia-1.7.3-linux-x86_64.tar.gz
RUN tar zxvf ./julia-1.7.3-linux-x86_64.tar.gz -C /julia/

# Add default user
RUN useradd -m -s /bin/bash -N -u $UID -g $GID $USER   \
    && chmod -R 775 /home/joules

# Remove sample keys
RUN rm -f /julia/julia-1.7.3/share/julia/stdlib/v1.7/LibGit2/test/keys/* \
          /julia/julia-1.7.3/stdlib/LibGit2/test/keys/*

# Container runtime state
USER $UID
CMD ["/julia/julia-1.7.3/bin/julia"]
HEALTHCHECK NONE
