#!/usr/bin/env Rscript

packagesToInstall = commandArgs(trailingOnly=TRUE)

for (package in packagesToInstall) {
#    # Installation from online
#    install.packages(package, dependencies=TRUE, repos='https://cran.rstudio.com/');
#    install.packages(package, dependencies=TRUE, repos='http://cran.us.r-project.org');
    install.packages(package, dependencies=TRUE, repos='https://packagemanager.rstudio.com/all/latest');

#    # Installation from local repo
#    install.packages(package, dependencies=TRUE, repos=NULL, recursive=TRUE, contriburl='file://tmp/repo/')
    if ( ! library(package, character.only=TRUE, logical.return=TRUE) ) {
        quit(status=1, save='no')
    }
}
