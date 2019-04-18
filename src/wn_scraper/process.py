import pandas as pd
from wn_scraper.webpage import get_7_day_forecast_image
from wn_scraper.ocr import get_text
from wn_scraper.data import get_wn_pop_data

def get_forecast_data(creds: str, forecast_url: str) -> pd.DataFrame:
  # Get the forecast image
  image_data = get_7_day_forecast_image(forecast_url)

  # Extract the text
  text = get_text(creds, image_data)

  # Extract the data
  data = get_wn_pop_data(text)

  return data