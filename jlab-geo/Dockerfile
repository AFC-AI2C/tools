FROM afcai2c/jlab-dl

USER root

RUN dnf clean all && \
    rm -rf /var/cache/dnf

RUN python3.8 -m pip install wheel \
			     pbr \
			     pygeos \
			     cython \
			     pyrobuf \
			     jupyterlab \
			     jupyterlab-git \
			     matplotlib \
			     geopandas \
			     geojson \
			     pysal \
			     mapclassify \
			     osmnx \
			     geopy \
			     rasterio \
			     contextily \
			     folium \
			     mplleaflet \
			     bokeh \
			     sphinx \
			     recommonmark \
			     pytest \
			     numpydoc \
			     h5py \
			     xmltodict \
			     tqdm \
			     numpy \
			     pillow \
			     sphinx_rtd_theme \
			     open-cv-plus \
			     pandas \
			     twine \
			     rtree \
			     psutil \
			     torchvision \
			     slidingwindow \
			     bumpversion \
			     sphinx-markdown-tables \
			     imagecodecs \
			     albumentations

USER 1001
WORKDIR $HOME

ENTRYPOINT ["tini", "-g", "--"]
CMD ["start-notebook.sh"]

EXPOSE 8282
HEALTHCHECK CMD pgrep "jupyter" > /dev/null || exit 1
