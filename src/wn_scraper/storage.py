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