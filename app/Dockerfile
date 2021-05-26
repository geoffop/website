FROM pypy:3 AS build
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
COPY requirements.txt .
ENV PATH="/venv/bin:$PATH"
RUN python3 -m venv /venv --system-site-packages &&\
    python3 -m pip install --no-cache-dir -r requirements.txt 

FROM pypy:3-slim
COPY --from=build /venv /venv
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"
ENV BIND_PORT 5000
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379
WORKDIR /app
COPY . .
EXPOSE $BIND_PORT
CMD python3 run.py