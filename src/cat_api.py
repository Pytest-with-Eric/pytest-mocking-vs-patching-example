import json
import logging
from typing import Tuple, Dict
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Get a logger instance for the module
logger = logging.getLogger(__name__)


class CatFact:
    def __init__(self):
        """
        Method to initialize the class with base URL
        """
        self.base_url = "https://meowfacts.herokuapp.com/"

    def _fetch_data(self, url) -> requests.models.Response:
        """
        Method to fetch data from URL
        """
        return requests.get(url)

    def get_cat_fact(self) -> Dict[str, any]:
        """
        Method to get API status
        """
        try:
            response = self._fetch_data(self.base_url)
            if response.status_code in (200, 201):
                return {
                    "status_code": response.status_code,
                    "response": response.json(),
                }
            else:
                return {
                    "status_code": response.status_code,
                    "response": {"ERROR": "Cat Fact Not Available"},
                }
        except requests.exceptions.RequestException as err:
            return {
                "status_code": None,
                "response": {"ERROR": "Request Exception occurred"},
            }


def main():
    cat_fact = CatFact()
    response = cat_fact.get_cat_fact()
    print(response)


if __name__ == "__main__":
    main()
