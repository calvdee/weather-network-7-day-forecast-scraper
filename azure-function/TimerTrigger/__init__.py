import os
import datetime
import logging

import azure.functions as func

from src.wn_scraper.process import get_forecast_data
from src.wn_scraper.storage import DataFrameAzureTableStorage

VISION_API_CREDS = os.environ['VISION_API_CREDS']
FORECAST_URL = os.environ['FORECAST_URL']
TABLE_STORAGE_ACCOUNT = os.environ['TABLE_STORAGE_ACCOUNT']
TABLE_STORAGE_CREDS = os.environ['TABLE_STORAGE_CREDS']

def run_process():
  data = get_forecast_data(VISION_API_CREDS, FORECAST_URL)
  storage = DataFrameAzureTableStorage(data)
  storage.save(TABLE_STORAGE_ACCOUNT, TABLE_STORAGE_CREDS)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Executing scraping process')

    run_process()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
