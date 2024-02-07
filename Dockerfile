FROM ubuntu:22.04
LABEL authors="calvinchai"

COPY ./ /app

WORKDIR /app

VOLUME /app/settings

RUN apt update
RUN apt install python3-all python3-pip -y
COPY static/GRADESCOPE_TEMPLATE/source/setup.sh /setup.sh
RUN /bin/bash -c "apt-get install -y build-essential libgtest-dev cmake && cd /usr/src/gtest && cmake CMakeLists.txt && make"
RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh

ENTRYPOINT ["/app/run.sh"]
