import requests 
import time
from typing import List
from urllib import parse

VISION_BASE_URL_V1 = 'https://canadacentral.api.cognitive.microsoft.com/vision/v1.0/'
VISION_BASE_URL_V2 = 'https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/'

def _get_operation_location_result(creds: str, image: str) -> str:
  """
  Uploads the image to the OCR service and returns a result.
  """
  # TODO: Handle errors
  or_result_url = VISION_BASE_URL_V1 + "recognizeText?handwriting=true"

  headers = {
    'Ocp-Apim-Subscription-Key': creds,
    'Content-Type': 'application/octet-stream'
  }

  response = requests.post(or_result_url, headers=headers, data=image)
  url = parse.urlparse(response.headers['Operation-Location'])
  operation_location = url.path.split('/')[-1]
  return operation_location

def _get_text_analysis(creds: str, operation_result_id: str) -> dict:
  """
  Attempts to retrieve the result until it's finished, returning the 
  resulting analysis object.
  """
  # TODO: Handle errors

  headers = {
    'Ocp-Apim-Subscription-Key': creds,
    'Content-Type': 'application/json'
  }
  n = 1
  result_url = VISION_BASE_URL_V2 + 'textOperations/' + operation_result_id
  
  print('Attempt #{} to retrieve text analysis'.format(n))
  response_json = requests.get(result_url, headers=headers).json()
  
  while response_json['status'] not in ['Succeeded', 'Failed']:
    n += 1
    # Wait for a bit
    time.sleep(0.5)
    # Try again
    print('Attempt #{} to retrieve text analysis'.format(n))
    response_json = requests.get(result_url, headers=headers).json()
  
  print('Retrieved text analysis in {} attempts'.format(n))
  return response_json

def get_text(creds: str, image: str) -> List[str]:
  """
  Identifies lines of text in the image using OCR and returns them in a list.

  Args:
    creds (str): Credentials used to access the OCR service
    image (str): A base64 encoded image.
  
  Returns:
    List[str]: Lines text extracted from the `image`.
  """
  id = _get_operation_location_result(creds, image)
  response = _get_text_analysis(creds, id)
  analysis = response['recognitionResult']
  lines = analysis['lines']

  get_text = lambda line: line['text']
  texts = list(map(get_text, lines))
  
  print('Extracted text from {} lines'.format(len(texts)))
  return texts