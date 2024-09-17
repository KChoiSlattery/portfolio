FROM debian:bullseye

RUN apt update && \
    apt clean && \
    apt install -y \
      git \
      npm \
      build-essential \
      ruby-full