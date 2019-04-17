import click

@click.group()
def cli():
  pass

@cli.command()
@click.argument('screenshot_path', default='screenshots')
def get_7_day_forecast(screenshot_path: str):
  from wn_scraper.webpage import save_7_day_forecast_image
  from datetime import datetime

  file_name = '7-day-forecast'
  screenshot_path = '{}/{}-{}.png'.format(
    screenshot_path,
    file_name, 
    datetime.now())

  save_7_day_forecast_image(True, True, screenshot_path)

if __name__ == '__main__':
  cli()