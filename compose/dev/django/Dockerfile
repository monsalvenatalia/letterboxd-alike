FROM python:3.11-slim

WORKDIR /app
COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/dev.txt

COPY . . 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]