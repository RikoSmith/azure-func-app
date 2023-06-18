import json
import logging
from json import JSONDecodeError

import azure.functions as func

from src.quote_api import QuoteAPI

quote_api = QuoteAPI()
quote_api._update_authors()


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    query = req.params.get("query")
    page = req.params.get("page")
    if not query:
        return func.HttpResponse(
            "{error: \"The 'query' param is required.\"}",
            status_code=400,
        )
    try:
        if page:
            result = quote_api.search_by_author(query, page=int(page))
        else:
            result = quote_api.search_by_author(query)
    except JSONDecodeError:
        return func.HttpResponse(
            json.dumps({
                "error": "Something went wrong!"
            }),
            status_code=500,
        )

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
    )
