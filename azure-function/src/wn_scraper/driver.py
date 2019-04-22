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
        
  options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  
  driver = webdriver.Chrome('/Users/calvindelima/bin/chromedriver-73', chrome_options=options)
  return driver