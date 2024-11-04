FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .  # This will copy all files, including script.py

CMD ["python", "script.py"]
