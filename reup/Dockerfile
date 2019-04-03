FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1

RUN set -e \
 && echo 'deb http://deb.debian.org/debian stretch non-free' >> /etc/apt/sources.list \
 && echo 'deb http://deb.debian.org/debian stretch-updates non-free' >> /etc/apt/sources.list \
 && echo 'deb http://security.debian.org stretch/updates non-free' >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/hoover
WORKDIR /opt/hoover

RUN cd /opt/hoover \
  && git clone https://96c48f089a06200e2eac4bbb03688b8b49e5e141@github.com/alexneamtu/reup.git

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