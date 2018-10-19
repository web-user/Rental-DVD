FROM python:3.6-jessie
RUN mkdir /dockyard
COPY . /dockyard/
WORKDIR /dockyard
RUN pip install -r requirements.txt
RUN apt-get install libjpeg-dev zlib1g-dev libpng12-dev
