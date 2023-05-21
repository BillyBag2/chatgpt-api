from ubuntu:22.04


RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get install -y python3-pip git figlet \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && pip install openai


