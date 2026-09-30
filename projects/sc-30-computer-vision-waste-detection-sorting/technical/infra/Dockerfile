FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY technical/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY technical/src ./src

ENV PYTHONPATH=/app/src

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
