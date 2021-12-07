FROM nginx:1.20.1
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    vim && \
    apt-get clean
COPY default.conf /etc/nginx/conf.d/default.conf