FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/hoover
WORKDIR /opt/hoover

RUN cd /opt/hoover \
  && git clone https://github.com/alexneamtu/reup.git

RUN cd /opt/hoover/reup \
  && pip install pipenv waitress \
  && pipenv install --system

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.3.0/wait /wait

RUN set -e \
 && echo '#!/bin/bash -e' > /runserver \
 && echo 'cd /opt/hoover/reup/reup' >> /runserver \
 && echo 'waitress-serve --port 8000 reup.wsgi:application' >> /runserver \
 && chmod +x /runserver /wait

CMD /wait && /runserver