FROM afcai2c/julia-base

USER root
RUN dnf upgrade -y --nodocs && \
    dnf clean all && \
    rm -rf /var/cache/dnf

RUN mkdir -p /ai-packages/
WORKDIR /ai-packages/
RUN curl http://coeusfileserver.usgovvirginia.cloudapp.usgovcloudapi.net/julia/julia-ai-packages.tar.gz --output julia-ai-packages.tar.gz
RUN tar xvf /ai-packages/julia-ai-packages.tar.gz --strip-components=2 -C /home/joules/
RUN rm -rf /ai-packages/

RUN rm -f \
/home/joules/.julia/packages/HTTP/aTjcj/test/resources/key.pem \
/home/joules/.julia/packages/MbedTLS/4YY6E/test/key.pem \
/home/joules/.julia/packages/MbedTLS/4YY6E/test/clntsrvr/test.key

USER "joules"
ENTRYPOINT ["/julia/julia-1.7.3/bin/julia"]
HEALTHCHECK NONE
