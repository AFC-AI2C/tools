FROM continuumio/miniconda3

RUN conda install jupyter -y --quiet && \
    mkdir -p /opt/notebooks

RUN conda install xeus-cling -y --quiet -c conda-forge
