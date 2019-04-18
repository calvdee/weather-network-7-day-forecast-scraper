from datetime import datetime
from src.wn_scraper.process import get_forecast_data
from support.constants import FORECAST_URL, CREDS

def test_run_process():
  data_path = 'data/'
  file_name = '{}/7-day-forecast-{}.csv'.format(
    data_path,
    datetime.now()
  )
  get_forecast_data(CREDS, FORECAST_URL).to_csv(file_name, index=False)


