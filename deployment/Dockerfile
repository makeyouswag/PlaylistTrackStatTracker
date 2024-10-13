FROM python:3.12
WORKDIR /usr/src/app

RUN apt -qq -y update && apt -y autoclean && apt -y autoremove && apt -y install nano tree
COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
