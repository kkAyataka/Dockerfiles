FROM ubuntu:26.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    git \
    ripgrep \
    jq \
    less \
    unzip \
    && rm -rf /var/lib/apt/lists/*

USER ubuntu
WORKDIR /work
RUN curl -fsSL https://claude.ai/install.sh | bash
ENTRYPOINT ["/bin/bash", "-l", "-c", "claude"]
#CMD
