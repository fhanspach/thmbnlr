FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential libjpeg-dev

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

ENTRYPOINT ["python"]
CMD ["main.py"]
