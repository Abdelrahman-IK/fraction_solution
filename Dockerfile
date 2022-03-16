FROM python:latest
ADD etl /usr/local/etl
WORKDIR /usr/local/etl
RUN pip install -r requirements.txt
CMD ["python", "-u", "/usr/local/etl/main.py"]