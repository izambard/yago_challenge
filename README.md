# Yago Challenge

# Environment installation

Using [Anaconda](https://www.anaconda.com/products/individual#Downloads) prompt :

`$ conda env create -f environment.yml`

This will create a Python 3.9 environment named `yago` with the required packages.
You have to activate the `yago` environment with the command:

`$ conda activate yago`

Note that the `yml` env file has been created from the conda export commad:

`conda env export --no-builds --name yago > environment.yml`

General [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) for reference.

# Environment variables

Environment variables are managed using a `.env` file in the development setup.
You have to create a `.env` file in development (see [python-dotenv](https://pypi.org/project/python-dotenv/)) with the following variables:

- CORS_ORIGIN=https://127.0.0.1:3000,http://127.0.0.1:3000,https://localhost:3000,http://localhost:3000

- YAGO_API_URL_ROOT=https://staging-gtw.seraphin.be
- YAGO_API_KEY=###GUESS#WHAT?###

The `.env` file is NOT part of the code base versionisation system (do not put it in git!).

# Running the service locally:

Running REST API service : `$ uvicorn service.api:app --log-config logging_config.ini --port 80 --host localhost --env-file .env`

Service can be called e.g. using `curl`: `$ curl "localhost/quotes/professional-liability/"  -H "Content-Type: application/json" -X POST --data @payload2.json`

# Running the service in a Docker container:

REST API in the container : 

`$ make run_api WEB_CONCURRENCY=1`

( `WEB_CONCURRENCY` specifies the number of process to start). 

[Make](https://www.gnu.org/software/make/) has to be insalled.

# Automatic Testing
Simply invoke `pytest` in the root of the repo:

`$ pytest`