FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 python3-dev  \
    alpine-sdk mariadb-dev postgresql-dev git \
    jpeg-dev zlib-dev libjpeg \
    && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools Pillow

WORKDIR /app

COPY . .

RUN git clone https://github.com/NaylsonFerreira/bicycle.git bicycle

WORKDIR /app/bicycle

RUN pip3 install --no-cache --upgrade -r requirements.txt 

EXPOSE 8000

RUN chmod +x run.sh
CMD ["sh","run.sh"]
# docker-compose up --build --remove-orphans
