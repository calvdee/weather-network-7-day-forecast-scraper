import pandas as pd
from src.wn_scraper.storage import DataFrameFileStorage

def test_file_storage_save_file_path(tmp_path):
  file_path = tmp_path / 'test_file_storage_save.csv'
  # with open(file_path, 'w') as f:
  #   f.write('bleh')
  
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