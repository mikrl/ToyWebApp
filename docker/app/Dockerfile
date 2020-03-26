FROM ubuntu:trusty

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY ./app/ /app/
COPY ./analysis/ /analysis/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000"]



