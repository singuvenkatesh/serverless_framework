import json


def hello(event, context):
    return dict(
        statusCode=200,
        body="hello welcome to Demo on serverless Framework"
    )
  
