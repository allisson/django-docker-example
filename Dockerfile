# Myblog
#
# VERSION               0.1

FROM allisson/docker-ubuntu:latest
MAINTAINER Allisson Azevedo <allisson@gmail.com>

# avoid debconf and initrd
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

# use myblog.settings_production
ENV DJANGO_SETTINGS_MODULE myblog.settings_production

# install packages
RUN apt-get update
RUN apt-get install -y git-core python-psycopg2 python-imaging python-pip supervisor

# setup app
RUN mkdir /deploy/
ADD myblog /deploy/myblog
RUN (cd /deploy/myblog && pip install -r requirements.txt)
RUN (cd /deploy/myblog && python manage.py syncdb --noinput)
RUN (cd /deploy/myblog && python manage.py migrate --noinput)
RUN (cd /deploy/myblog && python manage.py collectstatic --noinput)

# clean packages
RUN apt-get clean
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# expose mysql port
EXPOSE 8000

# copy supervisor conf
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# start supervisor
CMD ["/usr/local/bin/honcho -d /deploy/myblog -f Procfile start"]
