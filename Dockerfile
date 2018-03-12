FROM python:

WORKDIR /usr/src/app

RUN pip install flask

COPY ./src .

CMD [ "python", "./app.py" ]