# Pythonのベースイメージを作成
FROM python:3.9.0-slim

ENV PYTHONUNBUFFERD True

ENV APP_HOME /app
# 作業ディレクトリを指定
WORKDIR $APP_HOME
# アプリケーションファイルのコピー
COPY src ./src
COPY requirements.txt ./requirements.txt

# 依存関係をインストール
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get purge -y --auto-remove build-essential

# Uvicornを使用してアプリケーションを実行
CMD sh -c "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-8080}"
