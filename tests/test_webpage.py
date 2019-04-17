import sys, os, time
sys.path.insert(1, os.path.join(sys.path[0], '../src'))

from datetime import datetime
from src.wn_scraper.driver import get_driver
from src.wn_scraper.webpage import save_7_day_forecast_image, get_7_day_forecast_image
from support.constants import FORECAST_URL

def test_get_driver():
  driver = get_driver()

def test_save_7_day_forecast_image():
  screenshot_path = '{}/7-day-forecast-{}.png'.format('screenshots', datetime.now())
  save_7_day_forecast_image(FORECAST_URL, screenshot_path)
  time.sleep(5)

def test_get_forecast_image():
  image = get_7_day_forecast_image(FORECAST_URL)
  assert len(image) > 0