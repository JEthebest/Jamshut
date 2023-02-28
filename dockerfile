FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    postgresql-client

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD python manage.py makemigrations && python manage.py migrate && python manage.py first_csv --path markets/scripts/location.csv && python manage.py second_csv --path markets/scripts/product.csv