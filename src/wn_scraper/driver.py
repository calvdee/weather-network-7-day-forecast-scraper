import chromedriver_binary
from selenium import webdriver 

def get_driver(headless=True) -> webdriver.Chrome:
  """ Creates a Chrome web driver.

  Args:
    headless (bool): Whether the driver should create a GUI.

  Returns:
    selenium.WebDriver
  """
  options = webdriver.ChromeOptions()   
  options.add_argument('--ignore-certificate-errors')  

  if headless:
    options.add_argument('headless')  
        
  driver = webdriver.Chrome(chrome_options=options)
  return driver