@REM conda activate yago 

set REST_PORT=80
set LOGGING_CONFIG_FILE=logging_config.ini


start uvicorn service.api:app --log-config %LOGGING_CONFIG_FILE% --port %REST_PORT% --host localhost --env-file .env
