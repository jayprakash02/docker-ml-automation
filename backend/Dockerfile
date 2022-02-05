FROM python:3.8.8-slim-buster
ENV PYTHONUNBUFFERED=1
# RUN mkdir /app 
WORKDIR /app/backend/
ADD ./requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/backend/requirements.txt --no-cache-dir
COPY . .

ENV PORT 8000
# CMD python manage.py migrate --no-input
CMD python3 manage.py runserver 0.0.0.0:$PORT