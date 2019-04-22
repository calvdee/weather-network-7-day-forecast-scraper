import logging

class DataFrameFileStorage:
  def __init__(self: object, data: object) -> None:
    self.data = data

  def save(self, file_path=None, file=None, sep=',', index=False, **kwargs) -> None:
    kwargs['sep'] = sep
    kwargs['index'] = index

    if file_path is not None:
      self.data.to_csv(file_path, **kwargs)
    elif file is not None:
      self.data.to_csv(file, **kwargs)
    else:
      raise Exception('save requires `file_path` or `file`.')

    logging.info('Saved data to', file_path)

class DataFrameAzureTableStorage:
  def __init__(self, data: object) -> None:
    self.data = data

  def save(self, storage_account: str, key: str) -> None:
    from azure.cosmosdb.table.tableservice import TableService
    from azure.cosmosdb.table.models import Entity
    from azure.cosmosdb.table.tablebatch import TableBatch
    
    TABLE_NAME = 'WeatherNetworkForecasts'

    # Create the table storage object
    ts = TableService(account_name=storage_account, account_key=key)

    # Create the records from the data
    records = (
      self.data
        .assign(date_retrieved=lambda df: df['date_retrieved'].dt.date)
        .rename(columns={
          'date_retrieved': 'PartitionKey',
          'date_forecast': 'RowKey'
        })
        .astype(str)
        .to_dict(orient='records')
    )

    # Add the data to the batch and save it
    batch = TableBatch()
    list(map(batch.insert_entity, records))
    ts.commit_batch(TABLE_NAME, batch)

    logging.info('Saved {} records to {}'.format(len(records), TABLE_NAME))