FROM afcai2c/openjdk11:latest

USER root 

ENV FC_LANG en-US LC_CTYPE en_US.UTF-8
ARG MB_EDITION=oss

RUN useradd metabase && \
    usermod -u 1001 metabase && \
    yum update -y && \
    yum install -y fontconfig
RUN yum localinstall -y --nogpgcheck \
        http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/ca-certificates-2020.2.41-80.0.el8_2.noarch.rpm \
        https://vault.centos.org/centos/8/BaseOS/x86_64/os/Packages/dejavu-sans-fonts-2.35-7.el8.noarch.rpm

        #http://mirror.centos.org/centos/8/BaseOS/x86_64/os/Packages/dejavu-sans-fonts-2.35-7.el8.noarch.rpm
        
WORKDIR /etc/pki/ca-trust/source/anchors/

RUN chown metabase:metabase /etc/pki/ca-trust/source/anchors/ && \
    update-ca-trust force-enable && \
    update-ca-trust extract && \
    mkdir -p /plugins && \
    chmod a+rwx /plugins

# for reference, not needed
#    curl -LO https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem && \
#    curl -LO https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem && \

WORKDIR /app/

COPY ./scripts/entrypoint.sh .

RUN curl -LO https://downloads.metabase.com/v0.41.1/metabase.jar

USER 1001

WORKDIR /home/metabase

EXPOSE 3000

ENTRYPOINT ["sh","-c","/app/entrypoint.sh"]

HEALTHCHECK CMD curl localhost:3000 || exit 1
