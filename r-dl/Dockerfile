FROM rstudio:latest

USER root


# RUN python3.6 -m pip install --no-index --find-links . \
#     tensorflow                                         \
#     cuDNN                                              \
#     CUDA                                               \
#     keras

# RUN R -e "install.packages('reticulate')"
       

#RUN mkdir -p /tmp/repo/
#COPY *.tar.gz /tmp/repo/

# Creates local R repository from the /tmp/repo directory
#RUN R -e "tools::write_PACKAGES('/tmp/repo/')"

# Requested packages
#RUN R -e "install.packages(c('tidyverse', 'shiny', 'plotly', 'shinydashboard', 'DT', 'rmarkdown', 'flexdashboard'), repos='http://cran.r-project.org', INSTALL_opts='--no-html')"
#RUN R -e "install.packages(c('tensorflow', 'cuDNN', 'CUDA', 'keras','reticulate'), dependencies=TRUE, repos=NULL, recursive=TRUE, contriburl='file://tmp/repo/')"

# # curl -O https://download3.rstudio.org/centos7/x86_64/shiny-server-1.5.16.958-x86_64.rpm
# COPY shiny-server-1.5.16.958-x86_64.rpm .

# RUN yum -y install --nogpgcheck shiny-server-1.5.16.958-x86_64.rpm && \
# 	rm -rf shiny-server-1.5.16.958-x86_64.rpm

# RUN usermod shiny -g 0

# RUN mkdir -p /var/log/shiny-server /var/lib/shiny-server/bookmarks \
# 	&& chown shiny:shiny /var/log/shiny-server /var/lib/shiny-server/bookmarks \
# 	&& chown shiny:shiny -R /srv/shiny-server \
# 	&& chmod 755 -R /srv/shiny-server \
# 	&& chown shiny:shiny -R /opt/shiny-server/samples/sample-apps /var/lib/shiny-server/bookmarks \
# 	&& chmod 755 -R /opt/shiny-server/samples/sample-apps

# EXPOSE 3838

# # shiny account is created when installing the shiny rpm
# USER shiny

# ENTRYPOINT [ "/usr/bin/shiny-server" ]

# R Code that is ran within the container to download image specific packages and dependencies
# also shows their URL for later processing
# getDependencies <- function(packs){
#  dependencyNames <- unlist(
#    tools::package_dependencies(packages = packs, db = available.packages(), 
#                                which = c("Depends", "Imports"),
#                                recursive = TRUE))
#  packageNames <- union(packs, dependencyNames)
#  packageNames
# }
# packages <- getDependencies(c('tensorflow','cuDNN', 'CUDA', 'keras'))
# setwd(".")
# pkgInfo <- download.packages(pkgs = packages, destdir = getwd())


# Troubleshooting within R, check if packages are installed
# sessionInfo()
# packageVersion("shiny")

# Troubleshooting
# tail -f /var/log/shiny-server.log
# cat /etc/shiny-server/shiny-server.conf

#Tensorflow
# Keras_Preprocessing-1.1.2-py2.py3-none-any.whl
# Markdown-3.3.4-py3-none-any.whl
# Werkzeug-1.0.1-py2.py3-none-any.whl
# absl_py-0.12.0-py3-none-any.whl
# astunparse-1.6.3-py2.py3-none-any.whl
# cachetools-4.2.1-py3-none-any.whl
# certifi-2020.12.5-py2.py3-none-any.whl
# chardet-4.0.0-py2.py3-none-any.whl
# flatbuffers-1.12-py2.py3-none-any.whl
# gast-0.3.3-py2.py3-none-any.whl
# google_auth-1.28.0-py2.py3-none-any.whl
# google_auth_oauthlib-0.4.4-py2.py3-none-any.whl
# google_pasta-0.2.0-py3-none-any.whl
# grpcio-1.32.0-cp36-cp36m-manylinux2014_x86_64.whl
# h5py-2.10.0-cp36-cp36m-manylinux1_x86_64.whl
# idna-2.10-py2.py3-none-any.whl
# importlib_metadata-3.10.0-py3-none-any.whl
# numpy-1.19.5-cp36-cp36m-manylinux2010_x86_64.whl
# oauthlib-3.1.0-py2.py3-none-any.whl
# opt_einsum-3.3.0-py3-none-any.whl
# protobuf-3.15.6-cp36-cp36m-manylinux1_x86_64.whl
# pyasn1-0.4.8-py2.py3-none-any.whl
# pyasn1_modules-0.2.8-py2.py3-none-any.whl
# requests-2.25.1-py2.py3-none-any.whl
# requests_oauthlib-1.3.0-py2.py3-none-any.whl
# rsa-4.7.2-py3-none-any.whl
# setuptools-54.2.0-py3-none-any.whl
# six-1.15.0-py2.py3-none-any.whl
# tensorboard-2.4.1-py3-none-any.whl
# tensorboard_plugin_wit-1.8.0-py3-none-any.whl
# tensorflow-2.4.1-cp36-cp36m-manylinux2010_x86_64.whl
# tensorflow_estimator-2.4.0-py2.py3-none-any.whl
# termcolor-1.1.0.tar.gz
# typing_extensions-3.7.4.3-py3-none-any.whl
# urllib3-1.26.4-py2.py3-none-any.whl
# wheel-0.36.2-py2.py3-none-any.whl
# wrapt-1.12.1.tar.gz
# zipp-3.4.1-py3-none-any.whl


# Keras 
# Keras-2.4.3-py2.py3-none-any.whl	       
# h5py-3.1.0-cp36-cp36m-manylinux1_x86_64.whl
# PyYAML-5.4.1-cp36-cp36m-manylinux1_x86_64.whl  
# numpy-1.19.5-cp36-cp36m-manylinux2010_x86_64.whl
# cached_property-1.5.2-py2.py3-none-any.whl     
# scipy-1.5.4-cp36-cp36m-manylinux1_x86_64.whl

# CUDA
# cuda-0.0.1.tar.gz

# cuDNN
