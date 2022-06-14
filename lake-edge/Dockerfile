FROM python:3.9

USER root

RUN set -xeu && \
    apt update && \
    apt install -y -q vim && \
  # Install Python 3 packages
    pip3 install --upgrade --ignore-installed pip setuptools && \
    pip3 install  && \
    pip3 install --quiet \
     'trino[sqlalchemy]' \
     'dagster' \
     'dagit' \
     'great_expectations' && \
    groupadd bunbun --gid 1000 && \
    useradd bunbun --uid 1000 --gid 1000 && \
    mkdir -p /home/bunbun && \
    chown -R "bunbun:bunbun" /home/bunbun && \
  # Clean
    apt clean && \
    pip3 cache purge 

USER bunbun:bunbun

EXPOSE 8888

WORKDIR "${HOME}"
