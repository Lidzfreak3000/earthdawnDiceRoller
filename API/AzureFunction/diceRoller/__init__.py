import logging
import azure.functions as func

from .source.diceRoller.diceRoller import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    cmd = req.params.get('cmd').split(' ')
    response = step(cmd)

    if response:
        return func.HttpResponse(f"{response}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. There was an unknown error.",
             status_code=200
        )
 