FROM python:2.7

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8889

CMD ["python", "app.py", "-p", "8889"]