FROM ubuntu:22.04
LABEL authors="calvinchai"

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN apt update
RUN apt install python3-all python3-pip -y
RUN /bin/bash -c "apt-get install -y build-essential libgtest-dev cmake && cd /usr/src/gtest && cmake CMakeLists.txt && make"
RUN pip install -r requirements.txt

COPY ./ /app
VOLUME /app/settings

RUN python3 scripts/setup.py

RUN chmod +x /app/run.sh
ENTRYPOINT ["/app/run.sh"]
