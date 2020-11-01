FROM python:3.8

WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic

EXPOSE 8000
CMD ["uwsgi", "uwsgi.ini"]