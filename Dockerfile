FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


ENTRYPOINT [ "python","manage.py","runserver","0.0.0.0:8000" ]