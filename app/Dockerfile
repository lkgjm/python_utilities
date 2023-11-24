FROM python:3.11-alpine
LABEL authors="Gertjan van der Meulen"

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py
COPY ./templates /templates
COPY ./static static

RUN pip install -r /requirements.txt

EXPOSE $BIND_PORT

CMD ["python", "/app.py"]
