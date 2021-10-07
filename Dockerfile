FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN pip install django
COPY . /code/
CMD ["/usr/local/bin/python3", "/code/./manage.py", "runserver", "0.0.0.0:80"]