import json
import logging
from json import JSONDecodeError
from typing import Dict

import requests


class QuoteAPI:
    def __init__(self) -> None:
        self.base_url = "https://api.quotable.io/"
        self.author_slugs = set()
        self.last_author_slug = None

    def get_random_quote(self) -> Dict:
        response = requests.get(self.base_url + "random")
        logging.info(f"RESPONSE: {response}")
        return response.json()

    def search_by_author(self, query: str, page: int = 1) -> Dict:
        self._update_authors()
        authors = self._search_author_slug(query)
        logging.info(f"Found authors: {len(authors)}")
        response = requests.get(
            self.base_url + "quotes",
            params={
                "author": "|".join(map(str, authors[:50])),
                "page": page,
                "sortBy": "author",
            },
        )
        logging.info(f"RESPONSE: {response}")

        return response.json()

    def _update_authors(self):
        logging.info("Started retrieving authors...")
        authors_url = self.base_url + "authors"
        page = 1
        results = ["*"]
        first_author = None
        while results:
            logging.info(f"Page: {page}")
            response = requests.get(
                authors_url,
                params={"sortBy": "dateAdded", "limit": 500, "page": page},
            )
            results = response.json()["results"]
            if results:
                logging.info(f"Chunk: {len(results)}")
                new_authors = [author["slug"] for author in results]
                if page == 1:
                    first_author = new_authors[0]
                self.author_slugs.update(new_authors)
                page = page + 1
                if self.last_author_slug in new_authors:
                    logging.info(f"Reached known author. Stopping requests...")
                    break
        self.last_author_slug = first_author
        logging.info(f"Retrieved {len(self.author_slugs)} authors.")

    def _search_author_slug(self, query: str):
        return [item for item in self.author_slugs if query in item]
