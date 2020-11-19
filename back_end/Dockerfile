FROM python:3.8.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
COPY . /app/
WORKDIR /app
RUN pip install --upgrade -r requirements.txt
CMD ["sh", "-c", "gunicorn \
    -worker 3 \
    --max-requests 500 \
    --max-requests-jitter 50 \
    --bind 0.0.0.0:$RUN_PORT \
    app:app"]