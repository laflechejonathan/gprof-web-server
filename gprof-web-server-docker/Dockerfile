FROM gliderlabs/alpine:3.4

RUN apk add --no-cache bash nginx supervisor python wget && \
    wget --no-check-certificate -O \
    /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py && python /tmp/get-pip.py

ADD deploy /deploy/

RUN pip install -r /deploy/src/requirements.txt
RUN mkdir -p /var/log/supervisord/ && \
    mkdir -p /etc/nginx/sites-enabled && \
    cp /deploy/nginx.conf /etc/nginx/sites-enabled/nginx.conf && \
    cp /deploy/supervisor.conf /etc/supervisor.conf

EXPOSE 8000
CMD supervisord -n -c /etc/supervisor.conf
