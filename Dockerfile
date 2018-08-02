# Use an official perl as an image
FROM perl:5.20
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

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

WORKDIR /app
RUN pip install -r requirements.txt

# download and install from TEST-PyPI, so I don't need to make so many official releases
# will later be replaced with normal pypi installation
RUN pip install --index-url https://test.pypi.org/simple/ thoipapy


# Run app.py when the container launches
CMD python -W ignore app.py -i 00_test_input.txt -f ./


### docker commind line how to run docker_thoipapy
# cd C:/Users/ZENGBO/PycharmProjects/docker_thoipapy
# docker build -t thoipa .
# docker run thoipa
# docker system prune -a
# docker image ls --all
# docker export 4112ad985867 >contents.tar
# docker cp 22b60e8ac63c:/app/bnip3/THOIPA_out.csv ./output/output.csv
# docker cp 22b60e8ac63c:/app/bnip3/ ./output/