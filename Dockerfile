FROM debian:bullseye

RUN apt update && \
    apt clean && \
    apt install -y \
      build-essential \
      ruby-full