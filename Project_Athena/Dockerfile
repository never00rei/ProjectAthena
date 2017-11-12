# Use an official Python runtime as a parent image
FROM python:3.6.3-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV NAME World
ENV API_TOKEN None
ENV BOT-NAME Athena

# Run command.
CMD ["python3", "Athena/run.py"]
