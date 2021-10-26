#! /bin/bash

superset db upgrade
superset fab create-admin --firstname '' --lastname '' --email '' --username "$USERNAME" --password "$PASSWORD" 
superset init

if [[ -e "/etc/crt.d" && "$(ls -A /etc/crt.d)" ]]; then
    echo "Starting with https..."
    gunicorn                              \
        -w 10                             \
        --timeout 120                     \
        -b 0.0.0.0:8443                   \
        --limit-request-line 0            \
        --limit-request-field_size 0      \
        --certfile=/etc/crt.d/server.crt  \
        --keyfile=/etc/crt.d/server.key   \
        "superset.app:create_app()"
else
    echo "Starting with http..."
    gunicorn                         \
        -w 10                        \
        --timeout 120                \
        -b 0.0.0.0:8088              \
        --limit-request-line 0       \
        --limit-request-field_size 0 \
        "superset.app:create_app()"
fi
