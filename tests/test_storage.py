import pandas as pd
from src.wn_scraper.storage import DataFrameFileStorage, DataFrameAzureTableStorage
from support.creds import TABLE_STORAGE_ACCOUNT, TABLE_STORAGE_CREDS
from support.constants import WN_FORECAST_DATA_PATH
from support import get_text_data

def test_file_storage_save_file_path(tmp_path):
  file_path = tmp_path / 'test_file_storage_save.csv'

  data = pd.DataFrame({
    'a': [1,2],
    'b': [3,4]
  })

  storage = DataFrameFileStorage(data)
  storage.save(file_path=file_path)

  df = pd.read_csv(file_path)
  assert (df['a'] == df['a']).sum() == len(data)

def test_file_storage_save_file(tmp_path):
  file_path = tmp_path / 'test_file_storage_save.csv'
 
  data = pd.DataFrame({
    'a': [1,2],
    'b': [3,4]
  })

  storage = DataFrameFileStorage(data)
  storage.save(file_path=file_path)


  with open(file_path, 'w') as f:
    storage.save(file=f)

  df = pd.read_csv(file_path)
  assert (df['a'] == df['a']).sum() == len(data)

def test_table_storage_save():
  data = pd.read_csv(WN_FORECAST_DATA_PATH, parse_dates=['date_retrieved', 'date_forecast'])
  storage = DataFrameAzureTableStorage(data)
  storage.save(TABLE_STORAGE_ACCOUNT, TABLE_STORAGE_CREDS)