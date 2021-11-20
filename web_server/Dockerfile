FROM python:3.9-buster

# copy src code
RUN mkdir /web_server
WORKDIR /web_server/

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
