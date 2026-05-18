FROM python:3.11-alpine

WORKDIR /app
COPY requirment.txt .
RUN pip install -r requirment.txt
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
