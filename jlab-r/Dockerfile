FROM afcai2c/r-studio-dl:latest AS multi-stage2
FROM afcai2c/jlab-eda:latest

COPY --from=multi-stage2 /opt/R /opt/R
COPY --from=multi-stage2 /usr/lib64 /usr/lib64

USER root
#Note: reference the r-base or python-r-ai images, this is the version of R installed in those images
ARG R_VERSION=4.0.3 
RUN ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R                 && \
    ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript

COPY ./scripts/fix-permissions /fix-permissions
# COPY ./scripts/fix-permissions /fix-permissions
RUN chmod +x /fix-permissions                         && \
    /fix-permissions ${HOME} -P                       && \
    chmod -R 775 /opt/R/${R_VERSION}/lib/R/           && \
    rm -f /fix-permissions

RUN yum install -y \
    make    \
    gcc-c++ \
    # needed when displaying plot graphs that use fonts
    fontconfig

COPY ./ai-ml-packages.R /ai-ml-packages.R
COPY ./scripts/ai-ml-packages.R /ai-ml-packages.R

# https://github.com/IRkernel/IRkernel
RUN Rscript --no-save /ai-ml-packages.R \
    # Install R kernel for use in JupyterLab
    IRkernel

# to register the kernel in the current R installation   
RUN R -e "IRkernel::installspec()"

RUN curl -sL https://rpm.nodesource.com/setup_14.x | bash -   && \
    yum install -y nodejs

# for RStudio’s shortcuts
RUN jupyter labextension install @techrah/text-shortcuts  

# Install reticulate miniconda packages, apparently not included when R installing reticulate
RUN R -e "reticulate::install_miniconda()"

RUN yum install -y \
    make    \
    gcc-c++

# You can add other R kernel versions
#RUN R -e "IRkernel::installspec(name = 'ir40', displayname = 'R ${R_VERSION}')"

USER 1001

WORKDIR /home/jovyan

EXPOSE 8888

HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1o

