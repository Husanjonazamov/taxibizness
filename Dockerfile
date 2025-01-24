FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN chmod +x /code/entrypoint.sh  # Skriptga bajarish huquqini berish

CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000 && python3 bot.py"]
