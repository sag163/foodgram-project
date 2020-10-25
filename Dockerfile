FROM python:3.8

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

RUN python manage.py collectstatic --noinput

CMD gunicorn assistant_product.wsgi:application --bind 0.0.0.0:8000 