import pandas as pd
import re
import numpy as np
from datetime import datetime
from typing import List

# Extraction
get_text = lambda line: line['text']
to_int = lambda text: int(re.sub('[^0-9]', '', text))

# Predicates
contains_precip = lambda text: re.search(r'\d{1,} mm', text) is not None
contains_pop = lambda text: re.search(r'\d{1,} \%', text) is not None

def _get_dates(periods: int) -> pd.DataFrame():
  today = datetime.now().date()
  dates = pd.date_range(today, periods=periods)
  return dates

def get_wn_pop_data(texts: List[str]) -> pd.DataFrame:
  """Extracts PoP (probability of precipitation) and expected rain values from `texts`.

  Args:
    texts (List[str]): A list of text values from an OCR result.

  Returns:
    pandas.DataFrame: A dataframe with PoP and predicted precipitation
    levels for the next 7 days.
  """
  # Get the pops and precipitation values using predicates
  precips = list(filter(contains_precip, texts))
  pops = list(filter(contains_pop, texts))

   # Apply transformations
  int_pops = list(map(to_int, pops))
  int_precips = list(map(to_int, precips))

  # Create the dataframe
  periods = 7

  assert periods == len(int_pops)

  dates = _get_dates(periods)

  data = pd.DataFrame({
    'date_retrieved': pd.Series(np.repeat(datetime.now(), periods)),
    'date_forecast': dates,
    'prob': int_pops
  })

  return data