FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN pip install pytest

COPY . .

RUN python3 app.py

CMD ["python3", "main.py"]

#CMD echo " !! Cela veut dire que ça fonctionne !"