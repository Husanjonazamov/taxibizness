FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

COPY . /code/

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD bash -c "python manage.py runserver 0.0.0.0:8000 & python3 bot.py & wait"
