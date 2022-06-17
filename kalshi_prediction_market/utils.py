#From zip https://kalshi-public-docs.s3.amazonaws.com/KalshiAPIStarterCode.zip accessed on 6/15/2022
# linked from https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html
import requests
import json
from datetime import datetime as dt
from urllib3.exceptions import HTTPError
from dateutil import parser
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
from datetime import timedelta
import time


class KalshiClient:
    """A simple client that allows utils to call authenticated Kalshi API endpoints."""

    def __init__(
            self,
            host: str,
            email: str,
            password: str,
            token: Optional[str] = None,
            user_id: Optional[str] = None,
    ):
        """Initializes the client and logs in the specified user.

        Raises an HttpError if the user could not be authenticated.
        """

        self.host = host
        self.email = email
        self.password = password
        self.token = token
        self.user_id = user_id
        self.last_api_call = datetime.now()

    """Built in rate-limiter. We STRONGLY encourage you to keep 
    some sort of rate limiting, just in case there is a bug in your 
    code. Feel free to adjust the threshold"""

    def rate_limit(self) -> None:
        # Adjust time between each api call
        THRESHOLD_IN_MILLISECONDS = 1000

        now = datetime.now()
        threshold_in_microseconds = 1000 * THRESHOLD_IN_MILLISECONDS
        threshold_in_seconds = THRESHOLD_IN_MILLISECONDS / 1000
        if now - self.last_api_call > timedelta(microseconds=threshold_in_microseconds):
            time.sleep(threshold_in_seconds)
        self.last_api_call = datetime.now()

    def post(self, path: str, body: dict) -> Any:
        """POSTs to an authenticated Kalshi HTTP endpoint.

        Returns the response body. Raises an HttpError on non-2XX results.
        """
        self.rate_limit()

        response = requests.post(
            self.host + path, data=body, headers=self.request_headers()
        )
        self.raise_if_bad_response(response)
        return response.json()

    def get(self, path: str, params: Dict[str, Any] = {}) -> Any:
        """GETs from an authenticated Kalshi HTTP endpoint.

        Returns the response body. Raises an HttpError on non-2XX results."""
        self.rate_limit()

        response = requests.get(
            self.host + path, headers=self.request_headers(), params=params
        )
        self.raise_if_bad_response(response)
        return response.json()

    def request_headers(self) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = self.user_id + " " + self.token
        return headers

    def raise_if_bad_response(self, response: requests.Response) -> None:
        if response.status_code not in range(200, 299):
            raise HttpError(response.reason, response.status_code)


class HttpError(Exception):
    """Represents an HTTP error with reason and status code."""

    def __init__(self, reason: str, status: int):
        super().__init__(reason)
        self.reason = reason
        self.status = status

    def __str__(self) -> str:
        return "HttpError(%d %s)" % (self.status, self.reason)


class ExchangeClient(KalshiClient):
    def __init__(self, exchange_api_base: str, username: str, password: str):
        super().__init__(
            exchange_api_base,
            username,
            password,
        )

        """You must log in before making authenticated calls. We store the token and 
        pass it into each call."""
        login_json = json.dumps({"email": self.email, "password": self.password})
        result = self.post("/v1/log_in", login_json)

        self.token = result["token"]
        self.user_id = result["user_id"]
        self.markets_url = "/v1/markets"

    def get_market_url(self, market_id: str) -> str:
        return self.markets_url + "/" + market_id

    def get_market(self, market_id: str):
        base_url = self.get_market_url(market_id)
        dictr = self.get(base_url)
        return dictr

    def get_public_markets(self):
        dictr = self.get(self.markets_url)
        return dictr

    def get_orderbook(self, market_id: str):
        base_url = self.get_market_url(market_id)
        order_book_url = base_url + "/order_book"
        dictr = self.get(order_book_url)
        return dictr
