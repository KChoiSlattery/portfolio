FROM ubuntu

RUN apt update && \
    apt clean && \
    apt install -y \
      git \
      npm \
      build-essential \
      ruby-full \
      zlib1g-dev