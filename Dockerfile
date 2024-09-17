FROM ubuntu:24.04.1

RUN apt update && \
    apt clean && \
    apt install -y \
      git \
      npm \
      build-essential \
      ruby-full \
      zlib1g-dev

# These next few lines are just straight from the Jekyll docs at https://jekyllrb.com/docs/installation/ubuntu/
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
RUN source ~/.bashrc