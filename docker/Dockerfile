FROM python:3.8-slim-bullseye

ENV HOST_SRC=.
ENV CONTAINER_SRC=/wallet_generator
RUN apt-get -y update && \
    apt-get -y install \
    build-essential 

WORKDIR $CONTAINER_SRC

COPY $HOST_SRC/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
COPY $HOST_SRC .

WORKDIR $CONTAINER_SRC
RUN mv docker/initializer.sh /initializer.sh
RUN chmod +x /initializer.sh

EXPOSE 8000

ENTRYPOINT ["/initializer.sh"]
CMD ["init"]