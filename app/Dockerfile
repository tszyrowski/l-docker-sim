FROM python:3.9-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD ["python", "./server.py"]