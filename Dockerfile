FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/hoover
WORKDIR /opt/hoover

RUN pip install pipenv waitress

ADD Pipfile Pipfile.lock ./
RUN pipenv install --system

ADD reup ./reup
ADD runserver ./

CMD ./runserver
