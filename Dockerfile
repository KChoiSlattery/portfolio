FROM debian:bullseye

RUN apt update && \
    apt clean && \
    apt install -y \
      git \
      build-essential \
      ruby-full \
      npm