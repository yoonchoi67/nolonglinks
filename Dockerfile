FROM python:3

RUN pip install --upgrade pip
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./django-webapp /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]