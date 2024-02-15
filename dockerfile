FROM python:3.9-slim
WORKDIR /usr/src/app
COPY simple_exporter.py .
RUN pip3 install --no-cache-dir flask
CMD ["python3", "simple_exporter.py"]