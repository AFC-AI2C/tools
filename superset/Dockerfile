FROM afcai2c/python38-ai:latest

ARG USERNAME
ARG PASSWORD

USER root

RUN yum update -y && \
    yum clean all -y && \
    yum install -y \
        gcc \
        gcc-c++ \
        libffi-devel \
        python3-devel \
        python3-pip \
        python3-wheel \
        openssl-devel \
        cyrus-sasl-devel \
        openldap-devel

WORKDIR /tmp/repo

COPY *.tar.gz .
COPY *.whl .

RUN python3

RUN python3.8 -m pip install --upgrade \
        setuptools \
        pip && \
    python3.8 -m pip install \
        Pillow \
        apache-superset

# Copy supserset config into python path
# All the parameters and default values defined in https://github.com/apache/incubator-superset/blob/master/superset/config.py can be altered in your local superset_config.py
COPY ./scripts/superset_config.py /usr/local/lib/python3.8/site-packages/

RUN superset db upgrade && \
    export FLASK_APP=superset

COPY ./scripts/init_superset.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/init_superset.sh

# ##########################
# # Clean up install files #
# ##########################

RUN rm -rf /tmp/repo

RUN python3

WORKDIR $HOME

ENTRYPOINT ["bash","/usr/local/bin/init_superset.sh"]

EXPOSE 8088

HEALTHCHECK --interval=10s --timeout=1s CMD python.3.8 -c 'print("up")' || exit 1

#################
# local testing #
#################



##################################################
# Future Support for Databases other than SQLite #
##################################################
# # Install Database Drivers
# # https://superset.apache.org/docs/databases/installing-database-drivers
# # The following database support adds about .5 GB to the image
# RUN python3.8 -m pip install \
#     # Amazon Athena
#         PyAthenaJDBC>1.0.9        \
#         PyAthena>1.2.0	          \
#     # Amazon Redshift	
#         sqlalchemy-redshift       \
#     # Apache Drill	
#         sqlalchemy-drill          \
#     # Apache Druid	
#         pydruid                   \
#     # Apache Hive	
#         pyhive                    \
#     # Apache Impala	
#         impala                    \
#     # Apache Kylin	
#         kylinpy                   \
#     # Apache Pinot	
#         pinotdb                   \
#     # Apache Solr	
#         sqlalchemy-solr           \
#     # Apache Spark SQL	
#         pyhive                    \
#     # Azure MS SQL	
#         pymssql                   \
#     # Big Query	
#         pybigquery                \
#     # ClickHouse	
#         sqlalchemy-clickhouse     \
#     # CockroachDB
#         cockroachdb               \
#     # Elasticsearch	
#         elasticsearch-dbapi       \
#     # Google Sheets	
#         shillelagh[gsheetsapi]    \
#     # IBM Db2	
#         ibm_db_sa                 \
#     # Oracle	
#         cx_Oracle                 \
#     # Trino	
#         sqlalchemy-trino          \
#     # Presto	
#         pyhive                    \
#     # SAP Hana	
#         hdbcli                    \
#         sqlalchemy-hana           \
#         apache-superset[hana]     \
#     # Snowflake	
#         snowflake-sqlalchemy      \
#     # SQL Server	
#         pymssql                   \
#     # Teradata	
#         sqlalchemy-teradata       \
#     #Vertica	
#         sqlalchemy-vertica-python

# # MySQL	
# RUN yum localinstall -y mysql
#         #libedit-3.1-23.20170329cvs.el8.x86_64.rpm \
#         #mysql-8.0.21-1.module+el8.2.0+7855+47abd494.x86_64.rpm
#         #mysql-common-8.0.21-1.module+el8.2.0+7855+47abd494.x86_64.rpm
#         #mariadb-connector-c-config-3.1.11-2.el8_3.noarch.rpm  
# # PostgreSQL & Hologres
# RUN yum localinstall postgresql
#         #libpq-12.5-1.el8_3.x86_64.rpm
#         #libpq-12.5-1.el8_3.x86_64.rpm
#         #postgresql-10.15-1.module+el8.3.0+8944+1ca16b1f.x86_64.rpm

