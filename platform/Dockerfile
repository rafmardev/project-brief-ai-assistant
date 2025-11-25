FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["python", "-m", "worker.gemini_worker"]
EXPOSE 8000