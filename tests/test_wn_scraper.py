from datetime import datetime
from src.wn_scraper.process import get_forecast_data
from src.wn_scraper.storage import DataFrameAzureTableStorage
from support.creds import VISION_API_CREDS, TABLE_STORAGE_ACCOUNT, TABLE_STORAGE_CREDS
from support.constants import FORECAST_URL

def test_run_process():
  data_path = 'data/'
  file_name = '{}/7-day-forecast-{}.csv'.format(
    data_path,
    datetime.now()
  )
  get_forecast_data(VISION_API_CREDS, FORECAST_URL).to_csv(file_name, index=False)

def test_run_process_azure():
  data = get_forecast_data(VISION_API_CREDS, FORECAST_URL)
  storage = DataFrameAzureTableStorage(data)
  storage.save(TABLE_STORAGE_ACCOUNT, TABLE_STORAGE_CREDS)