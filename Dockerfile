# app/Dockerfile
# MUltistage build
# First Image
FROM python:3.9-slim AS compile-image

EXPOSE 8501

WORKDIR /app

ENV FLIT_ROOT_INSTALL=1
ARG PIP_DISABLE_PIP_VERSION_CHECK=1
ARG PIP_NO_CACHE_DIR=1

RUN apt-get update
RUN apt-get install -y --no-install-recommends software-properties-common
RUN rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install --no-cache-dir --upgrade pip

RUN pip3 install --no-cache-dir flit

COPY . /app

RUN flit install --deps production


FROM python:3.9-slim AS build-image

COPY --from=compile-image /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"


COPY . /app

WORKDIR /app

RUN mv /app/.streamlit ~/.streamlit

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "Curriculum_Vitae.py", "--server.port=8501", "--server.address=0.0.0.0"]
