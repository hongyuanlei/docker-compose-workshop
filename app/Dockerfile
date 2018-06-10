FROM django

RUN pip install --upgrade pip && pip install redis

ADD src /app

WORKDIR /app/redisweb

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8001"]