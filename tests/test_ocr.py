from src.wn_scraper.ocr import _get_operation_location_result, _get_text_analysis, get_text

with open('/Users/calvindelima/ldn-weekly-rain-day-predictions/tests/creds.txt', 'r') as f:
  creds =  f.readline()

image_path = '/Users/calvindelima/ldn-weekly-rain-day-predictions/tests/screenshot.png'

def test_ocr_operation_result():
  image = open(image_path, 'rb').read()
  result = _get_operation_location_result(creds, image)
  assert result not in [None, '']

def test_ocr_text_analysis():
  image = open(image_path, 'rb').read()
  result = _get_operation_location_result(creds, image)
  an = _get_text_analysis(creds, result)
  assert 'recognitionResult' in an.keys()

def test_ocr_get_text():
  image = open(image_path, 'rb').read()
  lines = get_text(creds, image)
  assert len(lines) > 0