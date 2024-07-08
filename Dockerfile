FROM python:3.12.3-slim
WORKDIR /app
COPY . .
CMD ["python3", "myproject.py"]
