FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

COPY ./app/ /app/
WORKDIR /app/

RUN pip install -r flask-serv-req.txt

#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000"]



