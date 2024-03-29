FROM ubuntu:22.04
LABEL authors="calvinchai"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y python3-all python3-pip
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash student
RUN chmod -R u-r /app


VOLUME /app/settings
VOLUME /app/workdir
VOLUME /app/output
VOLUME /app/webui/pages

COPY . .

RUN chmod +x /app/post_setup.sh && /app/post_setup.sh

RUN chmod +x /app/run.sh
ENTRYPOINT ["/app/run.sh"]
