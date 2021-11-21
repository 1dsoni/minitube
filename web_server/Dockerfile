FROM ubuntu:20.04

# copy src code
RUN mkdir /web_server
WORKDIR /web_server/

RUN apt -y update && apt -y install apt-utils && apt -y install net-tools python3.8 python3-pip mysql-client libmysqlclient-dev && apt -y upgrade

# just copy the requirements file and install
ADD ./requirements.txt /web_server/requirements.txt

# installing project requirements
RUN pip install -r /web_server/requirements.txt

# add the rest of code
ADD .. /web_server/

ENV PYTHONPATH "${PYTHONPATH}:/web_server/minitube/"

# makes sure logs are not missing when system crashes
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["/web_server/runner.sh"]
