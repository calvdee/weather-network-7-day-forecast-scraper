import click

@click.group()
def cli():
  pass

@cli.command()
@click.argument('creds', required=True)
@click.argument('furl', required=True)
@click.argument('dpath', required=False)
def get_7_day_forecast(creds: str, furl: str, dpath: str) -> None:
  from wn_scraper.process import get_forecast_data
  from datetime import datetime

  if dpath is None or dpath == '':
    dpath = 'data/7-day-forecast-{}.csv'.format(
      data_path,
      datetime.now()
    )

  data = get_forecast_data(creds, forecast_url)
  data.to_csv(dpath, index=False)

if __name__ == '__main__':
  cli()