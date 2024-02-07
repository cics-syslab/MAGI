FROM ubuntu:22.04
LABEL authors="calvinchai"

COPY ./ /app

WORKDIR /app

VOLUME /app/settings




ENTRYPOINT ["top", "-b"]


