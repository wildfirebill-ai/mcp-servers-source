FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY server.py skills.md ./
COPY data ./data
EXPOSE 25083
CMD ["python", "server.py"]
