# Use an official perl as an image
FROM perl:5.20

# FROM ubuntu:16.04

# FROM biocontainers/biocontainers:debian-stretch-backports
# MAINTAINER biocontainers <biodocker@gmail.com>
# LABEL    software="freecontact" \ 
#     container="freecontact" \ 
#     about.summary="fast protein contact predictor" \ 
#     about.home="http://rostlab.org/" \ 
#     software.version="1.0.21-5-deb" \ 
#     version="1" \ 
#     about.copyright="2013 Laszlo Kajan <lkajan@rostlab.org>, Technical University of Munich, Germany" \ 
#     about.license="GPL-3+" \ 
#     about.license_file="/usr/share/doc/freecontact/copyright" \ 
#     extra.binaries="/usr/bin/freecontact" \ 
#     about.tags=""

# ENV DEBIAN_FRONTEND noninteractive
# RUN apt-get update && apt-get install -y freecontact && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*
# USER biodocker

# FROM ubuntu

# ENV DEBIAN_FRONTEND noninteractive
# RUN apt-get update && \
#     apt-get -y install gcc mono-mcs && \
#     rm -rf /var/lib/apt/lists/*

# RUN apt-get update && \
#     apt-get -y install libboost-filesystem-dev libboost-thread-dev && \
#     rm -rf /var/lib/apt/lists/*

# ADD . /app

# WORKDIR /app/freecontact-1.0.21
# RUN  ./configure --enable-apache2=`which apxs` \
#     && make \
#     && make install
# RUN ./configure
# RUN make
 # RUN make install

# Use an official Python runtime as a parent image
FROM python:3.6-slim

RUN apt-get update && apt-get install -y --no-install-recommends tk-dev && rm -r /var/lib/apt/lists/*
RUN apt-get update \
    && apt-get --yes --no-install-recommends install \
        python3 python3-dev \
        python3-pip python3-venv python3-wheel python3-setuptools \
        build-essential \
        graphviz git \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends freecontact && rm -r /var/lib/apt/lists/*
# RUN git clone https://github.com/bojigu/thoipapy.git /app/

# RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
# RUN mkdir /build/lib
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# WORKDIR /app/freecontact-1.0.21
# RUN ./configure
# RUN make
# RUN make install

# WORKDIR /app/thoipapy
# # Install any needed packages specified in requirements.txt
# RUN python setup.py develop

WORKDIR /app
RUN pip install -r requirements.txt
# download and install from TEST-PyPI, so I don't need to make so many official releases
RUN pip install --index-url https://test.pypi.org/simple/ thoipapy

# Define environment variable
# ENV NAME World
# ENV DISPLAY :0

# Run app.py when the container launches
CMD python -W ignore app.py -i input.txt -f ./

#cd C:/Users/ZENGBO/PycharmProjects/thoipapy_docker
#docker build -t friendlyhello .
#docker run friendlyhello
#docker system prune -a
#docker image ls --all
#docker export 4112ad985867 >contents.tar
#docker cp 22b60e8ac63c:/app/bnip3/THOIPA_out.csv ./output