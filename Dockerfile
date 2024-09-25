FROM python:3.12.2-slim-bullseye
COPY . .
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "script.py"]
