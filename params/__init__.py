import os
import logging

LOGGER = logging.getLogger(__name__)

def toBool(x) -> bool:
    return x in ("True","true",True,1)

# Backend
CORS_ORIGIN  : str = os.getenv("CORS_ORIGIN") or ""

# Caching
USE_FILE_CACHE : bool= toBool(os.getenv('USE_FILE_CACHE', False))
CACHE_DIR : str = os.getenv('CACHE_DIR') or './tmp'
S3_CACHE_BUCKET : str = os.getenv('S3_CACHE_BUCKET')
S3_CACHE_FOLDER : str = os.getenv('S3_CACHE_FOLDER', None)

# Business
YAGO_API_URL_ROOT : str = os.getenv('YAGO_API_URL_ROOT', 'https://staging-gtw.seraphin.be')
YAGO_API_KEY : str = os.getenv('YAGO_API_KEY', None)

LOGGER.info( "########################################################################")
LOGGER.info( "######                        PARAMS                               #####")
LOGGER.info(f'######   CORS_ORIGIN           : {CORS_ORIGIN}                              ')
LOGGER.info( "######                                                             #####")
LOGGER.info( "######                                                             #####")
LOGGER.info(f'######   USE_FILE_CACHE        : {USE_FILE_CACHE}                       ')
LOGGER.info(f'######   CACHE_DIR             : {CACHE_DIR}                            ')
LOGGER.info(f'######   S3_CACHE_BUCKET       : {S3_CACHE_BUCKET}                      ')
LOGGER.info(f'######   S3_CACHE_FOLDER       : {S3_CACHE_FOLDER}                      ')
LOGGER.info( "######                                                             #####")
LOGGER.info(f'######   YAGO_API_KEY          : {YAGO_API_KEY}                      ')
LOGGER.info( "########################################################################")

