from src.wn_scraper.ocr import _get_operation_location_result, _get_text_analysis, get_text
from support.constants import CREDS, IMAGE_PATH

def test_ocr_operation_result():
  image = open(IMAGE_PATH, 'rb').read()
  result = _get_operation_location_result(CREDS, image)
  assert result not in [None, '']

def test_ocr_text_analysis():
  image = open(IMAGE_PATH, 'rb').read()
  result = _get_operation_location_result(CREDS, image)
  an = _get_text_analysis(CREDS, result)
  assert 'recognitionResult' in an.keys()

def test_ocr_get_text():
  image = open(IMAGE_PATH, 'rb').read()
  lines = get_text(CREDS, image)
  assert len(lines) > 0