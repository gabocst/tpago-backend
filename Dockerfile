FROM python:3.7
RUN apt-get update && apt-get install -y gettext --no-install-recommends && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cd tpaga && python manage.py collectstatic --no-input
EXPOSE 8000
CMD gunicorn --chdir tpaga --bind :8000 --reload tpaga.wsgi:application
