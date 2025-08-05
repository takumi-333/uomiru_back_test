## 概要
このリポジトリは、ウオミルのBEをFlaskを用いて実装したものです。
Docker上で起動できる環境を提供しています。

## 📦 前提条件
- [Docker](https://www.docker.com/)がインストールされていること

## 🚀 起動方法

1. dockerイメージをbuild
  `flask-app`の部分は任意のタグをつけられます
```cli
docker-compose build --no-
```

2. dockerイメージからコンテナを起動
```cli
docker-compose up
```