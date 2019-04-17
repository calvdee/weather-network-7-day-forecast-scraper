from datetime import datetime
from src.wn_scraper.driver import get_driver
from src.wn_scraper.webpage import get_7_day_forecast_image
from src.wn_scraper.ocr import get_text
from src.wn_scraper.data import get_wn_pop_data

forecast_url = 'https://www.theweathernetwork.com/ca/14-day-weather-trend/ontario/london'

def get_forecast_data() -> None:
  # Get the forecast image
  image_data = get_7_day_forecast_image(forecast_url)

  # Run the OCR
  with open('/Users/calvindelima/ldn-weekly-rain-day-predictions/tests/creds.txt', 'r') as f:
    creds =  f.readline()

  # Extract the text
  text = get_text(creds, image_data)

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


