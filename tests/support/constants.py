CREDS = ''

with open('/Users/calvindelima/code/weekly-rain-day-predictions/weather-network-7-day-forecast-scraper/tests/creds.txt', 'r') as f:
  CREDS =  f.readline()

IMAGE_PATH = '/Users/calvindelima/code/weekly-rain-day-predictions/weather-network-7-day-forecast-scraper/tests/screenshot.png'
FORECAST_URL = 'https://www.theweathernetwork.com/ca/14-day-weather-trend/ontario/london'