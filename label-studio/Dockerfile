FROM afcai2c/python38-ai:latest


ARG LABEL_STUDIO_USERNAME
ARG LABEL_STUDIO_PASSWORD

RUN python3.8 -m pip install label-studio 

#ENV LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true

USER root

RUN ln -s /home/default/.local/bin/label-studio /bin

ENV LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true

COPY scripts/docker-entrypoint.sh /docker-entrypoint.sh

COPY conf/nginx.conf /etc/nginx/nginx.conf

RUN dnf upgrade -y && \
    # Install package
    rpm --import https://nginx.org/keys/nginx_signing.key && \
    yum localinstall -y https://nginx.org/packages/mainline/centos/8/x86_64/RPMS/nginx-1.21.1-1.el8.ngx.x86_64.rpm && \
    dnf install -y gettext && \

    # Create necessary directories
    mkdir -p /docker-entrypoint.d/ && \
    mkdir -p /etc/nginx/templates && \

    # Fix nginx user permissions (user auto-created during rpm installation)
    touch /var/cache/nginx/nginx.pid && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx && \
    chown -R nginx:nginx /var/cache/nginx/nginx.pid && \
    chown -R nginx:nginx /docker-entrypoint.d && \
   
    # Cleanup installation
    dnf clean all && \
    rm -rf /var/cache/dnf && \

    # Forward nginx logs to stdout and stderr
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

RUN cp -r /usr/share/nginx/html /etc/nginx && \
    rm /etc/nginx/conf.d/default.conf

COPY scripts/10-listen-on-ipv6-by-default.sh scripts/20-envsubst-on-templates.sh scripts/30-tune-worker-processes.sh /docker-entrypoint.d/

RUN chown -R nginx:nginx /docker-entrypoint.d && \
     # Remove Write permission
#     chmod o-w etc/pki/ca-trust/source/anchors/Certificates_PKCS7_v5.7_DoD.pem && \
     chmod o-w etc/nginx/nginx.conf && \
     chmod o-w docker-entrypoint.d/10-listen-on-ipv6-by-default.sh && \
     chmod o-w docker-entrypoint.d/30-tune-worker-processes.sh && \
     chmod o-w docker-entrypoint.d/20-envsubst-on-templates.sh && \
     chmod o-w docker-entrypoint.sh 
    
RUN usermod -u 1002 python  && \
    usermod -u 1001 nginx

USER nginx

EXPOSE 8080 8443

HEALTHCHECK --interval=10s --timeout=5s --start-period=1m --retries=5 CMD curl -I -f --max-time 5 http://localhost:8080 || curl -fsk https://localhost:8443 || exit 1

ENTRYPOINT ["/docker-entrypoint.sh"]

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]