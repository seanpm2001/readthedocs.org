FROM ubuntu:22.04

ARG GITHUB_USER
ARG GITHUB_TOKEN

ENV DEBIAN_FRONTEND noninteractive
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get -y update
RUN apt-get -y install \
        curl \
        g++ \
        git-core \
        libevent-dev \
        libpq-dev \
        libxml2-dev \
        libxslt1-dev \
        locales \
        build-essential \
        python3-pip \
        python3-dev \
        libmysqlclient-dev \
        libfreetype6 \
        libjpeg-dev \
        postgresql-client \
        sqlite \
        netcat \
        telnet \
        lsb-release

# Uncomment en_US.UTF-8 locale and generate it
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen

RUN pip3 install --no-cache-dir --upgrade pip

# Ensure that ``python`` is in the PATH so that ``./manage.py`` works
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /tmp

COPY requirements/pip.txt pip.txt
COPY requirements/debug.txt debug.txt
COPY requirements/docker.txt docker.txt
RUN pip3 install --no-cache-dir -r docker.txt

# Install readthedocs-ext only if GITHUB_TOKEN is provided
WORKDIR /usr/src/app/checkouts/
RUN if [ -n "$GITHUB_TOKEN" ] ; \
        then \
        git clone --depth 1 https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/readthedocs/readthedocs-ext ; \
        pip3 install --no-cache-dir -e readthedocs-ext ; \
        git clone --depth 1 https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/readthedocs/ext-theme ; \
        pip3 install --no-cache-dir -e ext-theme ; \
        fi

WORKDIR /usr/src/app/checkouts/readthedocs.org
