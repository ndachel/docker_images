FROM mesosphere/jenkins:3.0.2-2.32.2

ENV HTTP_PROXY "http://web-proxy.corp.hpecorp.net:8080"
ENV HTTPS_PROXY "http://web-proxy.corp.hpecorp.net:8080"
ENV http_proxy "http://web-proxy.corp.hpecorp.net:8080"
ENV https_proxy "http://web-proxy.corp.hpecorp.net:8080"

WORKDIR /usr/share/jenkins
RUN cp jenkins.war /usr/share/jenkins/war/jenkins.war
WORKDIR /usr/share/jenkins/war
RUN jar xvf jenkins.war
