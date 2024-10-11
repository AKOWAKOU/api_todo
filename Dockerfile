FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app/
RUN python -m venv venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt
EXPOSE 5002
CMD ["./venv/bin/python", "app.py"]
