FROM afcai2c/r-studio:latest

#USER root

#RUN python3.6 -m pip install --no-index --find-links . \
# RUN python3.8 -m pip install \
#     tensorflow                                         
# RUN python3.8 -m pip install \
#     cuDNN                                              
# RUN python3.8 -m pip install \
#     CUDA                                               
# RUN python3.8 -m pip install \
#     keras

#RUN R -e "install.packages(c('reticulate'), dependencies=TRUE, repos=NULL, recursive=TRUE, contriburl='file://tmp/repo/')"
RUN R -e "install.packages(c('utf8', 'pillar', 'vctrs', 'mime', 'glue', 'stringi', 'base64enc', 'diffobj', 'fansi', 'rematch2', 'tibble', 'processx', 'markdown', 'stringr', 'yaml', 'xfun', 'htmltools', 'tinytex', 'brio', 'cli', 'digest', 'ellipsis', 'lifecycle', 'magrittr', 'pkgload', 'ps', 'rlang', 'waldo', 'jsonlite', 'rappdirs', 'Rcpp', 'callr', 'knitr', 'rmarkdown', 'testthat','reticulate'), dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest')"
#RUN R -e "install.packages(c('utf8'), dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest')"

ENTRYPOINT [ "rstudio-server","start" ]
#ENTRYPOINT ["bash"]
 
HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

EXPOSE 8787

USER 1001


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
# packages <- getDependencies(c('reticulate'))
# packages <- getDependencies(c('tensorflow','cuDNN', 'CUDA', 'keras', 'reticulate'))
# setwd(".")
# pkgInfo <- download.packages(pkgs = packages, destdir = getwd())

