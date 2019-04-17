from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from .driver import get_driver
from datetime import datetime

def _move_to_element(driver, id: str) -> WebElement:
  """Uses the `driver` to scroll to the `ID`"""
  el = driver.find_element_by_id('fourteen-day-periods') 
  actions = ActionChains(driver)
  actions.move_to_element(el).perform()
  return el

def _save_screenshot(driver, path: str) -> None:
  """Uses the `driver` to save the screenshot at the `path`."""
  driver.save_screenshot(path)

def _get_screenshot_data(driver) -> None:
  """
  Returns the screenshot as base64 encoded data.
  """
  return driver.get_screenshot_as_png()

def save_7_day_forecast_image(forecast_url: str, screenshot_path: str, headless=True) -> None:
  """Downloads an image, optionally using a real browser window and
  saves the image to `screenshot_path`.

  Args:
    screenshot_path (str): The destination screenshot file path.
    headless (bool): Whether the driver should create a GUI.
  """
  driver = get_driver(headless=headless)
  print('Getting webpage')
  driver.get(forecast_url)      

  print('Navigating to element')
  forecast_el = _move_to_element(driver, 'fourteen-day-periods')

  assert screenshot_path is not None
  print('Saving screenshot')
  _save_screenshot(driver, screenshot_path)
  print('Saved screenshot to {}'.format(screenshot_path))

  driver.close()

  return screenshot_path

def get_7_day_forecast_image(forecast_url: str, headless=True) -> None:
  """Downloads an image, optionally using a real browser window and returns the
  image as binary data.

  Args:
    headless (bool): Whether the driver should create a GUI.
  """
  driver = get_driver(headless=headless)
  print('Getting webpage')
  driver.get(forecast_url)      

  print('Navigating to element')
  forecast_el = _move_to_element(driver, 'fourteen-day-periods')

  image_data = _get_screenshot_data(driver)
  print('Took screenshot')

  return image_data