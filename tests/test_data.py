from src.wn_scraper.data import get_wn_pop_data

def test_get_wn_pop_data():
  pops = [
    '90 %',
    '80 %',
    '70 %',
    '60 %',
    '50 %',
    '40 %',
    '30 %'
  ]

  precips = [
    '10 mm',
    '9 mm',
    '8 mm',
    '7 mm'
  ]

  data = get_wn_pop_data(pops + precips)

  # Only keeping pop values for now
  assert len(data) == len(pops)
  print(data)