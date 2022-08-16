FROM python:3.8-slim

COPY requirements.txt .

RUN set -ex; \
  	pip install --no-cache-dir -r requirements.txt

ADD tempgen.py .

CMD ["python", "-u", "./tempgen.py"]

# docker build -t tempgen .
# docker run -it --rm tempgen