FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y libpq-dev gcc \
    && pip install -r requirements.txt
CMD ["python", "app.py"]
