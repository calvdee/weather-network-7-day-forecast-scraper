FROM mcr.microsoft.com/azure-functions/python:2.0

WORKDIR /tmp
RUN apt-get update \
  && apt-get install -y libxss1 libappindicator1 libindicator7 \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install -y ./google-chrome*.deb

WORKDIR /home
COPY src src/
COPY tests tests/
COPY requirements.txt .
RUN pip3 install -r requirements.txt