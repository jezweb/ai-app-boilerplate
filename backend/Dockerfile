# Stage 1: Build dependencies
FROM python:3.11-slim as builder
WORKDIR /app
RUN pip install --no-cache-dir pip-tools
COPY requirements.in requirements-dev.in ./
RUN pip-compile requirements.in -o requirements.txt
RUN pip-compile requirements-dev.in -o requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final application image
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app/app
EXPOSE 8000
# The command is now in docker-compose.yml to enable hot-reloading
