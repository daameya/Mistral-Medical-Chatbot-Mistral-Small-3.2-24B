FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]