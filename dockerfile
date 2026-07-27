FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

EXPOSE 8000

CMD ["gunicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]