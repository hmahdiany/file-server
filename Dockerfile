FROM python:3.8.12-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /file-server

WORKDIR /file-server

ADD requirements.txt .

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /file-server/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ADD . .

RUN mkdir -p iso/media
 
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]