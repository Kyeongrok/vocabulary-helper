import json
from urllib.parse import unquote
from libs.naver_en_dict import getMean

try:
  import unzip_requirements
except ImportError:
  pass

def vocabulary(event, context):
    result = ""
    try:
        word = unquote(event['pathParameters']['word'])
    except Exception as e:
        word = ""

    response = {
        "statusCode": 200,
        "body": "<html><body>{}</body></html>".format(getMean(word))
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
