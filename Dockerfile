FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/hoover
WORKDIR /opt/hoover

RUN pip install pipenv waitress

ADD reup ./reup
ADD Pipfile Pipfile.lock runserver ./

RUN pipenv install --system

CMD ./runserver
