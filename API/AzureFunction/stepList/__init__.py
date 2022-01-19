import logging
import json
import azure.functions as func
from .constants import steps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Serializing json
    json_object = json.dumps(steps, indent = 4) 

    return func.HttpResponse(
        json_object,
        status_code=200
    )
