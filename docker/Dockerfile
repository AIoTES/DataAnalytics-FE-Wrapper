FROM python:3.7-slim

RUN apt update && apt install -y gcc libc-dev unixodbc-dev

COPY requirements.txt /app/src/requirements.txt
RUN pip install --no-cache-dir --trusted-host=pypi.python.org -r /app/src/requirements.txt

COPY ./src /app/src
COPY ./resources /app/resources

ENV PYTHONPATH /app
WORKDIR "/app/src"

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main"]
