# app/Dockerfile
FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

ENV FLIT_ROOT_INSTALL=1
ARG PIP_DISABLE_PIP_VERSION_CHECK=1
ARG PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir flit

COPY . /app

RUN flit install --deps production

RUN mv /app/.streamlit ~/.streamlit

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Curriculum_Vitae.py", "--server.port=8501", "--server.address=0.0.0.0"]
