from datetime import datetime
from src.wn_scraper.driver import get_driver
from src.wn_scraper.webpage import get_7_day_forecast_image
from src.wn_scraper.ocr import get_text
from src.wn_scraper.data import get_wn_pop_data
from support.constants import FORECAST_URL, CREDS

def get_forecast_data() -> None:
  # Get the forecast image
  image_data = get_7_day_forecast_image(FORECAST_URL)

  # Extract the text
  text = get_text(CREDS, image_data)

  # Extract the data
  data = get_wn_pop_data(text)

  return data

def test_run_process():
  data_path = 'data/'
  file_name = '{}/7-day-forecast-{}.csv'.format(
    data_path,
    datetime.now()
  )
  get_forecast_data().to_csv(file_name, index=False)


