FROM nginx:latest

RUN mkdir work && \
    cd work && \
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
        -sha256 -days 365 -passout pass:password -subj "/C=JP/ST=Ishikawa/L=Dokoka/O=Nanika/CN=https.server.test" && \
    echo "password" > /work/password

COPY ./https.conf /etc/nginx/conf.d/

CMD nginx -g "daemon off;"
