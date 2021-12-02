FROM python:3.9.7-slim-bullseye
WORKDIR /usr/src

# 必要パッケージのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    vim && \
    apt-get clean

# 必要ライブラリインストール
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir \
    Flask==2.0.1 \
    gunicorn==20.1.0 \