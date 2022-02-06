FROM python:3.8-slim-buster

RUN apt-get update
RUN mkdir ./coin-analyst

COPY . ./coin-analyst


WORKDIR coin-analyst
COPY ./scripts .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "simple_analysis.py"]