FROM ubuntu

ENV http_proxy=http://web-proxy.corp.hpecorp.net:8080
ENV https_proxy=http://web-proxy.corp.hpecorp.net:8080

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9D6D8F6BC857C906
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7638D0442B90D010
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7638D0442B90D010
RUN apt-get update -y --fix-missing
RUN apt-get install -y curl
RUN apt-get install -y iputils-ping
RUN apt-get install -y net-tools 
RUN sh -c '/bin/echo -e "Y" | apt-get install -y nginx'
RUN useradd nginx

ADD ./files/index.html /usr/share/nginx/html/index.html
ADD ./files/default.conf /etc/nginx/conf.d/default.conf
ADD ./files/nginx.conf /etc/nginx/nginx.conf

ADD ./files/index.html /usr/share/nginx/html/index.html
ADD ./files/about.html /usr/share/nginx/html/about.html
ADD ./files/contact.html /usr/share/nginx/html/contact.html
ADD ./files/order.php /usr/share/nginx/html/order.php
ADD ./files/health.html /usr/share/nginx/html/health.html
ADD ./files/info.php /usr/share/nginx/html/info.php

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80

CMD sed -e "s/CONTAINERID/'$(hostname)'/g" /usr/share/nginx/html/index.html > /usr/share/nginx/html/index.html.tmp && mv /usr/share/nginx/html/index.html.tmp /usr/share/nginx/html/index.html && nginx -g "daemon off;"
