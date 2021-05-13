FROM afcai2c/python38-ai:latest as multi-stage

# Going to copy over staged python packages into the next image

FROM afcai2c/r-base:latest

# # Copies over the virtual environment containing python3.8 and all the AI/ML python packages
COPY --from=multi-stage /opt/* /opt/
COPY --from=multi-stage /opt/Python-3.8.9/ /opt/Python-3.8.9/

# USER root

# # Fix that allows you to use python3.8
# RUN ln -sf /opt/Python-3.8.9/python /opt/python/venv/bin/python3.8

# # Makes the python packages accessable
# ENV PATH="/opt/python/venv/bin:$PATH"


# RUN yum upgrade -y       \ 
#     && yum install -y    \
#         vim              \
#         zip              \
#         unzip            \
#         wget             \
#         curl             \
#         net-tools        \
#         gcc-c++          \
#         git              \
#         # The following packages were removed from the parent image to mitigate vulnerabiliites, but are needed here to install R packages and will be remove again later
#         binutils         \
#         glibc-devel      \
#         glibc-headers    \
#         libcurl-devel    \
#         libX11 	         \
#         libX11-common 	 \
#         kernel-headers   \
#         # Needed to install various R packages
#         openssl-devel    \
#         libxml2-devel  


# USER default


# # R Script to install pacakges and provides a stop error if in installation fails
# COPY scripts/ai-ml-packages.R .


# # Note:
# #install.packages(c('broom','C50','cli','DT','ECharts2Shiny','feather','flexdashboard','forcats','foreign','gt','highcharter','htmlwidgets','httr','kernlab','kknn','knitr','lattice','lubridate','magrittr','Matrix','mlbench','nlme','nnet','openxlsx','packrat','parsnip','plotly','plotROC','randomForest','RCurl','rmarkdown','roxygen2','rvest','scales','shiny','shinydashboard','shinyWidgets','sparklyr','stringr','testthat','tidymodels','tidytext','xgboost','readr','readxl','tidyverse','timetk','devtools','ggiraph','flextable','kableExtra','leaflet','plumber','reticulate','rgdal','RJDBC','xpm'), dependencies=TRUE, repos = 'https://packagemanager.rstudio.com/all/latest')
# #'SQUAREM', 'caTools', 'triebeard', 'lava', 'inline', 'loo', 'gmp', 'polynom', 'sets', 'mathjaxr', 'rbibutils', 'gplots', 'rngWELL', 'misc3d', 'tmvnsim', 'miscTools', 'pcaPP', 'gdata', 'geometries', 'jsonify', 'rapidjsonr', 'sfheaders', 'urltools', 'httpcode', 'protolite', 'sys', 'miniUI', 'R.utils', 'showimage', 'fontBitstreamVera', 'fontLiberation', 'credentials', 'prodlim', 'lhs', 'snakecase', 'reactR', 'extraDistr', 'rstan', 'rstantools', 'fansi', 'pkgconfig', 'Formula', 'numDeriv', 'bdsmatrix', 'mvtnorm', 'flexmix', 'modeltools', 'partitions', 'Rdpack', 'xergm.common', 'sna', 'ROCR', 'RSiena', 'statnet.common', 'carData', 'abind', 'pbkrtest', 'rio', 'ModelMetrics', 'pROC', 'rex', 'gtools', 'plotrix', 'proxy', 'estimability', 'BiasedUrn', 'pander', 'trust', 'lpSolve', 'rle', 'dreamerr', 'gtable', 'isoband', 'shape', 'gridExtra', 'htmlTable', 'cobs', 'doParallel', 'randtoolbox', 'RcppArmadillo', 'FNN', 'multicool', 'plot3D', 'mnormt', 'pbivnorm', 'minqa', 'nloptr', 'statmod', 'RcppEigen', 'prediction', 'dfidx', 'TH.data', 'ucminf', 'maxLik', 'scatterplot3d', 'SparseM', 'MatrixModels', 'conquer', 'msm', 'fit.models', 'rrcov', 'DEoptimR', 'furrr', 'spData', 'deldir', 'LearnBayes', 'gmodels', 'mitools', 'quadprog', 'strucchange', 'urca', 'libcoin', 'inum', 'jquerylib', 'prismatic', 'rematch2', 'TTR', 'colorspace', 'geojsonsf', 'crul', 'V8', 'geojson', 'jqr', 'askpass', 'manipulateWidget', 'filehash', 'sysfonts', 'showtextdb', 'systemfonts', 'textshaping', 'R.cache', 'tensorflow', 'tfruns', 'zeallot', 'plotmo', 'TeachingDemos', 'reshape', 'debugme', 'parsedate', 'rematch', 'webdriver', 'fontquiver', 'freetypeharfbuzz', 'classInt', 'units', 'repr', 'bit', 'listenv', 'parallelly', 'fresh', 'waiter', 'gert', 'whisker', 'DiceDesign', 'gower', 'ipred', 'GPfit', 'hardhat', 'SnowballC', 'slam', 'fastmatch', 'RcppParallel', 'lda', 'matrixStats', 'ISOcodes', 'downloader', 'influenceR', 'cyclocomp', 'xmlparsedata', 'gargle', 'ids', 'utf8', 'warp', 'PerformanceAnalytics', 'Quandl', 'riingo', 'alphavantager', 'janitor', 'StanHeaders', 'reactable', 'progressr', 'prophet', 'xopen', 'clisymbols', 'gitcreds', 'ini', 'downlit', 'whoami', 'xslt', 'locatexec', 'plogr', 'leafem', 'leafpop', 'satellite', 'backports', 'dplyr', 'ellipsis', 'generics', 'glue', 'purrr', 'rlang', 'tibble', 'tidyr', 'AER', 'akima', 'AUC', 'bbmle', 'betareg', 'biglm', 'binGroup', 'btergm', 'car', 'caret', 'cmprsk', 'coda', 'covr', 'drc', 'e1071', 'emmeans', 'epiR', 'ergm', 'fixest', 'gam', 'gee', 'geepack', 'ggplot2', 'glmnet', 'glmnetUtils', 'gmm', 'Hmisc', 'irlba', 'joineRML', 'Kendall', 'ks', 'Lahman', 'lavaan', 'leaps', 'lfe', 'lm.beta', 'lme4', 'lmodel2', 'lmtest', 'lsmeans', 'maps', 'maptools', 'margins', 'mclust', 'mediation', 'metafor', 'mfx', 'mlogit', 'modeldata', 'modeltests', 'muhaz', 'multcomp', 'network', 'orcutt', 'ordinal', 'plm', 'poLCA', 'psych', 'quantreg', 'Rchoice', 'rgeos', 'robust', 'robustbase', 'rsample', 'sandwich', 'sp', 'spdep', 'spatialreg', 'speedglm', 'spelling', 'survey', 'systemfit', 'tseries', 'vars', 'zoo', 'partykit', 'Cubist', 'callr', 'mockery', 'ps', 'rstudioapi', 'prettycode', 'withr', 'htmltools', 'jsonlite', 'crosstalk', 'promises', 'bslib', 'testit', 'Rcpp', 'hms', 'checkmate', 'commonmark', 'fs', 'sass', 'tidyselect', 'paletteer', 'RColorBrewer', 'webshot', 'xml2', 'rlist', 'assertthat', 'xts', 'quantmod', 'igraph', 'yaml', 'rjson', 'viridisLite', 'gapminder', 'forecast', 'geojsonio', 'curl', 'mime', 'openssl', 'R6', 'httpuv', 'jpeg', 'png', 'evaluate', 'highr', 'markdown', 'xfun', 'formatR', 'digest', 'rgl', 'tikzDevice', 'tinytex', 'JuliaCall', 'magick', 'gifski', 'DBI', 'showtext', 'ragg', 'styler', 'latticeExtra', 'vctrs', 'expm', 'zip', 'stringi', 'globals', 'prettyunits', 'keras', 'earth', 'ranger', 'base64enc', 'lazyeval', 'data.table', 'hexbin', 'ggthemes', 'GGally', 'shinytest', 'vdiffr', 'Cairo', 'listviewer', 'dendextend', 'sf', 'IRdisplay', 'processx', 'plotlyGeoAssets', 'palmerpenguins', 'gridSVG', 'plyr', 'survivalROC', 'bitops', 'XML', 'tufte', 'dygraphs', 'rsconnect', 'brew', 'desc', 'pkgload', 'R.methodsS3', 'R.oo', 'lifecycle', 'selectr', 'repurrrsive', 'webfakes', 'farver', 'lab__eling', 'munsell', 'bit64', 'dichromat', 'xtable', 'sourcetools', 'later', 'crayon', 'fastmap', 'cachem', 'reactlog', 'future', 'shinydashboardPlus', 'bs4Dash', 'argonR', 'argonDash', 'tablerDash', 'blob', 'config', 'dbplyr', 'forge', 'r2d3', 'rappdirs', 'rprojroot', 'uuid', 'arrow', 'diffobj', 'foreach', 'iterators', 'janeaustenr', 'nycflights13', 'reshape2', 'brio', 'praise', 'waldo', 'diffviewer', 'usethis', 'conflicted', 'dials', 'infer', 'recipes', 'tune', 'workflows', 'workflowsets', 'yardstick', 'hunspell', 'tokenizers', 'tm', 'quanteda', 'wordcloud', 'topicmodels', 'NLP', 'mallet', 'stm', 'textdata', 'stopwords', 'DiagrammeR', 'Ckmeans.1d.dp', 'vcd', 'lintr', 'float', 'titanic', 'clipr', 'BH', 'cpp11', 'cellranger', 'progress', 'dtplyr', 'googledrive', 'googlesheets4', 'haven', 'modelr', 'pillar', 'reprex', 'padr', 'slider', 'anytime', 'timeDate', 'tidyquant', 'modeltime', 'robets', 'fracdiff', 'timeSeries', 'memoise', 'pkgbuild', 'rcmdcheck', 'remotes', 'rversions', 'sessioninfo', 'BiocManager', 'foghorn', 'gh', 'gmailr', 'pingr', 'pkgdown', 'rhub', 'gdtools', 'officer', 'bookdown', 'equatags', 'svglite', 'formattable', 'sparkline', 'raster', 'viridis', 'leaflet.providers', 'RJSONIO', 'webutils', 'sodium', 'swagger', 'visNetwork', 'RSQLite', 'mapview', 'rJava'
#     # 552 packages


# # R Packages can have a slow build time because they compile during installation - so build time is included for my sanity and expectation management
# # The ai-ml-packages.R script produces an error and stops the build if the R packages doesn't install
# RUN Rscript --no-save ai-ml-packages.R broom
# RUN Rscript --no-save ai-ml-packages.R C50
# RUN Rscript --no-save ai-ml-packages.R cli
# RUN Rscript --no-save ai-ml-packages.R DT
# RUN Rscript --no-save ai-ml-packages.R ECharts2Shiny
# RUN Rscript --no-save ai-ml-packages.R feather
# RUN Rscript --no-save ai-ml-packages.R flexdashboard
# RUN Rscript --no-save ai-ml-packages.R forcats
# RUN Rscript --no-save ai-ml-packages.R foreign
# RUN Rscript --no-save ai-ml-packages.R gt
# RUN Rscript --no-save ai-ml-packages.R highcharter
# RUN Rscript --no-save ai-ml-packages.R htmlwidgets
# RUN Rscript --no-save ai-ml-packages.R httr
# RUN Rscript --no-save ai-ml-packages.R kernlab
# RUN Rscript --no-save ai-ml-packages.R kknn
# RUN Rscript --no-save ai-ml-packages.R knitr
# RUN Rscript --no-save ai-ml-packages.R lattice
# RUN Rscript --no-save ai-ml-packages.R lubridate
# RUN Rscript --no-save ai-ml-packages.R magrittr
# RUN Rscript --no-save ai-ml-packages.R Matrix
# RUN Rscript --no-save ai-ml-packages.R mlbench
# RUN Rscript --no-save ai-ml-packages.R nlme
# RUN Rscript --no-save ai-ml-packages.R nnet
# RUN Rscript --no-save ai-ml-packages.R openxlsx
# RUN Rscript --no-save ai-ml-packages.R packrat
# RUN Rscript --no-save ai-ml-packages.R parsnip
# RUN Rscript --no-save ai-ml-packages.R plotly
# RUN Rscript --no-save ai-ml-packages.R plotROC
# RUN Rscript --no-save ai-ml-packages.R randomForest
# RUN Rscript --no-save ai-ml-packages.R RCurl
# RUN Rscript --no-save ai-ml-packages.R rmarkdown
# RUN Rscript --no-save ai-ml-packages.R roxygen2
# RUN Rscript --no-save ai-ml-packages.R rvest
# RUN Rscript --no-save ai-ml-packages.R scales
# RUN Rscript --no-save ai-ml-packages.R shiny
# RUN Rscript --no-save ai-ml-packages.R shinydashboard
# RUN Rscript --no-save ai-ml-packages.R shinyWidgets
# RUN Rscript --no-save ai-ml-packages.R sparklyr
# RUN Rscript --no-save ai-ml-packages.R stringr
# RUN Rscript --no-save ai-ml-packages.R testthat
# RUN Rscript --no-save ai-ml-packages.R tidymodels
# RUN Rscript --no-save ai-ml-packages.R tidytext
# RUN Rscript --no-save ai-ml-packages.R xgboost
# RUN Rscript --no-save ai-ml-packages.R readr
# RUN Rscript --no-save ai-ml-packages.R readxl
# RUN Rscript --no-save ai-ml-packages.R tidyverse
# RUN Rscript --no-save ai-ml-packages.R timetk


# # Copy in rpms
# COPY *.rpm .


# # Used npm to install xpm - not an R package
# USER root
# RUN yum install -y npm                 && \
#     npm install --global xpm@latest


# # reticulate R package
# USER root
# RUN yum install -y      \
#         libpng-devel    \
#         libpng
# USER default
# RUN Rscript --no-save ai-ml-packages.R reticulate 


# # plumber R package
# USER root
# RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-devel-1.0.18-2.el8.x86_64.rpm   && \
#     curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/l/libsodium-1.0.18-2.el8.x86_64.rpm
# RUN yum localinstall --nogpgcheck --skip-broken -y   \
#         libsodium-devel-1.0.18-2.el8.x86_64.rpm      \
#         libsodium-1.0.18-2.el8.x86_64.rpm
# USER default
# RUN Rscript --no-save ai-ml-packages.R plumber


# # kableExtra R package
# USER root
# RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/i/ImageMagick-c++-devel-6.9.10.86-1.el8.x86_64.rpm   && \
#     yum localinstall --nogpgcheck --skip-broken -y            \
#         ImageMagick-c++-devel-6.9.10.86-1.el8.x86_64.rpm   && \
#     yum install -y                                            \
#         fontconfig-devel
# USER default
# RUN Rscript --no-save ai-ml-packages.R kableExtra  


# # RJDBC R package
# USER root
# RUN yum install -y                     \
#         java-1.8.0-openjdk             \
#         java-1.8.0-openjdk-devel    && \
#     R CMD javareconf
# USER default
# RUN Rscript --no-save ai-ml-packages.R RJDBC  


# # leaflet package
# RUN Rscript --no-save ai-ml-packages.R leaflet


# # install pandoc
# USER root
# RUN curl -LO https://fossies.org/linux/www/pandoc-2.13-linux-amd64.tar.gz   && \
#     tar xvzf pandoc-2.13-linux-amd64.tar.gz --strip-components 1 -C /usr/local


# # devtools R package
# USER root
# RUN curl -LO http://mirror.centos.org/centos/8/PowerTools/x86_64/os/Packages/libgit2-devel-0.26.8-2.el8.i686.rpm    && \
#     curl -LO http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/harfbuzz-devel-1.7.5-3.el8.x86_64.rpm   && \
#     yum localinstall --nogpgcheck --skip-broken -y   \
#         libgit2-devel-0.26.8-2.el8.i686.rpm          \
#         harfbuzz-devel-1.7.5-3.el8.x86_64.rpm
# USER default
# RUN Rscript --no-save ai-ml-packages.R devtools

# # COPY install_r_packages.R .

# # # ggiraph R package #################### still trouble shooting ####################
#     # dependencies: 
# # USER root
# # RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/u/udunits2-devel-2.2.26-5.el8.x86_64.rpm   && \
# #     curl -LO http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/cairo-devel-1.15.12-3.el8.i686.rpm                        && \
# #     curl -LO http://repo.okay.com.mx/centos/8/x86_64/release/cairo-1.15.12-3.el8.x86_64.rpm                                           && \
# #     curl -LO http://mirror.centos.org/centos/7/os/x86_64/Packages/libXrender-devel-0.9.10-1.el7.x86_64.rpm                            && \
# #     curl -LO http://mirror.centos.org/centos/7/os/x86_64/Packages/pixman-devel-0.34.0-1.el7.x86_64.rpm                                && \
# #     curl -LO http://mirror.centos.org/centos/7/os/x86_64/Packages/libXext-devel-1.3.3-3.el7.x86_64.rpm
# # RUN yum localinstall --nogpgcheck --skip-broken -y   \
# #         udunits2-devel-2.2.26-5.el8.x86_64.rpm       \
# #         cairo-devel-1.15.12-3.el8.i686.rpm           \
# #         cairo-1.15.12-3.el8.x86_64.rpm               \
# #         libXrender-devel-0.9.10-1.el7.x86_64.rpm     \
# #         pixman-devel-0.34.0-1.el7.x86_64.rpm         \
# #         libXext-devel-1.3.3-3.el7.x86_64.rpm      && \
# #     export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/lib64/pkgconfig/freetype2.pc
# # USER default
# # RUN Rscript --no-save install_r_packages.R ggiraph


# # # flextable R package #################### still trouble shooting ####################
#     # dependencies: 
# # USER root
# # RUN yum install -y libxslt-devel
# # USER default
# # RUN Rscript --no-save install_r_packages.R flextable


# # rgdal R package #################### still trouble shooting ####################
#     # dependencies: 
# # USER root
# # RUN curl -LO https://download-ib01.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/g/gdal-3.0.4-5.el8.x86_64.rpm  && \
# #     yum localinstall --skip-broken -y gdal-3.0.4-5.el8.x86_64.rpm
# # USER default
# # RUN Rscript --no-save install_r_packages.R rgdal


# ########################
# # Cleanup and Finalize #
# ########################

# USER root

# RUN rm -rf /tmp/repo/

# USER default

# WORKDIR $HOME

# # every 10 seconds execute the R command specified to show 'healthy'
# HEALTHCHECK --interval=10s --timeout=1s CMD Rscript -e 'print("up")' || exit 1

# #################
# # Test Commands #
# #################
# # import sqlite3
# # import plotly
# # import pandas
# # import matplot
# # import seaborn
# # import numba
# # import numpy
# # import scipy
# # import sklearn
# # import tqdm
# # import urllib3
# # import requests
# # from bs4 import BeautifulSoup
# # from wordcloud import WordCloud
# # import statsmodels
# # import prophet
# # import django
# # import flask
# # R -e 'ls()'
# # R -e 'round(3.14159,2)'
# # library('broom')
# # library('C50')
# # library('cli')
# # library('DT')
# # library('ECharts2Shiny')
# # library('feather')
# # library('flexdashboard')
# # library('forcats')
# # library('foreign')
# # library('gt')
# # library('highcharter')
# # library('htmlwidgets')
# # library('httr')
# # library('kernlab')
# # library('kknn')
# # library('knitr')
# # library('lattice')
# # library('lubridate')
# # library('magrittr')
# # library('Matrix')
# # library('mlbench')
# # library('nlme')
# # library('nnet')
# # library('openxlsx')
# # library('packrat')
# # library('parsnip')
# # library('plotly')
# # library('plotROC')
# # library('randomForest')
# # library('RCurl')
# # library('rmarkdown')
# # library('roxygen2')
# # library('rvest')
# # library('scales')
# # library('shiny')
# # library('shinydashboard')
# # library('shinyWidgets')
# # library('sparklyr')
# # library('stringr')
# # library('testthat')
# # library('tidymodels')
# # library('tidytext')
# # library('xgboost')
# # library('readr')
# # library('readxl')
# # library('tidyverse')
# # library('timetk')
# # library('devtools')
# # library('ggiraph')
# # library('flextable')
# # library('kableExtra')
# # library('leaflet')
# # library('plumber')
# # library('reticulate')
# # library('rgdal')
# # library('RJDBC')
# # library('xpm')