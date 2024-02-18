# Dockerfile

FROM python:3.11-slim
USER root
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY python .

CMD ["python", "./main.py"]