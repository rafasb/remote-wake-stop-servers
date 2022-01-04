FROM ubuntu:latest
LABEL MANTAINER="Rafael Santisteban"

RUN apt-get update 
RUN apt-get -y install python3 python3-pip python3.8-venv sshpass sudo
RUN pip3 install --upgrade pip

RUN mkdir /api
RUN useradd -m api
USER api
WORKDIR /home/api/

ADD ./build-config/ ./
RUN pip install -r requirements.txt --user 

#Preparación del sistema
USER root
ENV PATH=/home/api/.local/bin:${PATH}
RUN chown -R api:api /home/api

USER api

CMD [ "python3","main.py" ]
