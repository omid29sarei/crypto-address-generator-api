FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /wallet_generator
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /wallet_generator/

RUN mv docker/initializer.sh /initializer.sh
RUN chmod +x /initializer.sh

EXPOSE 8000

ENTRYPOINT ["/initializer.sh"]
CMD ["init"]