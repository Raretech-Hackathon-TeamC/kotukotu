FROM python:3.10.10-buster as builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir app
WORKDIR /app
RUN mkdir -p tmp/sockets
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . .


# runner
FROM python:3.10.10-slim-buster as production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir app
WORKDIR /app
RUN mkdir -p tmp/sockets

RUN apt update \
    && apt install -y libpq5 libxml2 libmariadbclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=builder /app /app

# CMD uwsgi --ini uwsgi.ini
CMD ["uwsgi", "--ini", "uwsgi.ini"]