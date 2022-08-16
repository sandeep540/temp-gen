FROM python:3.8-slim

COPY requirements.txt .

RUN set -ex; \
  	pip install --no-cache-dir -r requirements.txt

ADD tempgen.py .

CMD ["python", "-u", "./tempgen.py"]

# docker build -t tempgen .
# docker run --network=host -it --rm tempgen 

#KAFKA_BROKERS=localhost:54595,localhost:54601,localhost:54600