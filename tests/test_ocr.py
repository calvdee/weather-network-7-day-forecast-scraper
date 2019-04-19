from src.wn_scraper.ocr import _get_operation_location_result, _get_text_analysis, get_text
from support.creds import VISION_API_CREDS
from support.constants import IMAGE_PATH

def test_ocr_operation_result():
  image = open(IMAGE_PATH, 'rb').read()
  result = _get_operation_location_result(VISION_API_CREDS, image)
  assert result not in [None, '']

def test_ocr_text_analysis():
  image = open(IMAGE_PATH, 'rb').read()
  result = _get_operation_location_result(VISION_API_CREDS, image)
  an = _get_text_analysis(VISION_API_CREDS, result)
  assert 'recognitionResult' in an.keys()

def test_ocr_get_text():
  image = open(IMAGE_PATH, 'rb').read()
  lines = get_text(VISION_API_CREDS, image)
  assert len(lines) > 0