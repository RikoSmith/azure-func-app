import json
import logging

import azure.functions as func

from src.quote_api import QuoteAPI


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Random quote requested.')

    quote_api = QuoteAPI()
    result = quote_api.get_random_quote()

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
    )
