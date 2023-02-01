FROM continuumio/miniconda3

WORKDIR /yago
COPY ./deployment/docker_environment.yml .
COPY ./deployment/docker.env .
RUN conda env create -f docker_environment.yml

ENV PYTHONPATH='$PYTHONPATH:./'
ENV PORT=80

COPY . .

EXPOSE 80

CMD conda run --no-capture-output -n yago python -m uvicorn service.api:app  --port $PORT --host 0.0.0.0