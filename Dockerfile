FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]