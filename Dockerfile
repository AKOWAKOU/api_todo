FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install the virtual environment and dependencies
RUN python -m venv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install -r requirements.txt

# Expose the port on which the Flask app will run
EXPOSE 5002

# Run the application
CMD ["./venv/bin/python", "app.py"]
