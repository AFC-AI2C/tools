# Nginx 

## What is nginx?
Nginx (pronounced "engine-x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause BSD-like license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.

By default this image will display `Hello Nginx ${VERSION}`

For more information visit http://nginx.org/en/docs/

  
### Run:  
`docker run -p 80:8080 -p 443:8443 <image name>` 

Exposes 8080 & 8443

### Hosting some simple static content

`docker run --name some-nginx -v /some/content:/etc/nginx/html:ro -d nginx`

Alternatively, a simple Dockerfile can be used to generate a new image that includes the necessary content (which is a much cleaner solution than the bind mount above):

`FROM nginx`
`COPY static-html-directory /usr/share/nginx/html`

Place this file in the same directory as your directory of content ("static-html-directory"), run docker build -t some-content-nginx ., then start your container:

`docker run --name some-nginx -d some-content-nginx`