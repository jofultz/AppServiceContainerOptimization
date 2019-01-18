#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip


RUN apt-get update
RUN apt-get install -y apt-utils

#add ssh support
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends openssh-server \
#    && echo "root:Docker!" | chpasswd
#
#COPY sshd_config /etc/ssh/
#EXPOSE 2222 80
#
#COPY init_container.sh /opt/startup
#
#RUN chmod 755 /opt/startup
#
#ENTRYPOINT ["/opt/startup/init_container.sh"]

#disto info
RUN cat /etc/issue

ENV LISTEN_PORT=80

EXPOSE 80


COPY /app /app
