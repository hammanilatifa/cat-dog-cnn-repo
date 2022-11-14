FROM ubuntu

RUN apt install epel-release -y
RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-devel -y
RUN apt install python3-pip -y
RUN mkdir /data
RUN mkdir /Code
RUN mkdir /Model

COPY /data/  /data/

RUN pip3 install -r /data/lib.txt

