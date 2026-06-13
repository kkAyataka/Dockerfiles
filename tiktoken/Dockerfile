FROM python:3.14.6-slim

RUN groupadd -g 1000 mint && \
    useradd -m -u 1000 -g mint -s /bin/bash mint

RUN pip install tiktoken==0.13.0

RUN python -c "import tiktoken; tiktoken.get_encoding('o200k_base')"

COPY entrypoint.py /entrypoint.py

USER mint
WORKDIR /work
ENTRYPOINT ["python", "/entrypoint.py"]
#CMD
