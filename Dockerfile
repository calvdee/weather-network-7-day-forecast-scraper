FROM mcr.microsoft.com/azure-functions/python:2.0

# Install Chrome
WORKDIR /tmp

RUN apt-get update \
  && apt-get install -y libxss1 libappindicator1 libindicator7 \
  && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install -y ./google-chrome*.deb

# Copy function code
COPY azure-function/ /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt

# Enable logging
ENV AzureFunctionsJobHost__Logging__Console__IsEnabled=true