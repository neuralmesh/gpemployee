# docker/Dockerfile

FROM python:3.8-slim
WORKDIR /usr/src/app

# Install dependencies
COPY docker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and docs
COPY src/ ./src/
COPY docs/ ./docs/

EXPOSE 8000
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]

