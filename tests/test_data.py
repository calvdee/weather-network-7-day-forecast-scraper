from support import get_text_data
from src.wn_scraper.data import get_wn_pop_data

def test_get_wn_pop_data():
  text_data = get_text_data()

  pops = list(filter(lambda text: '%' in text, text_data))

  data = get_wn_pop_data(text_data)

  # Only keeping pop values for now
  assert len(data) == len(pops)