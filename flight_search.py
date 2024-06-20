import os
from dotenv import load_dotenv
import requests

AM_TOKEN_ENDPOINT="https://test.api.amadeus.com/v1/security/oauth2/token"
AM_GET_BY_CITY_ENDPOINT="https://test.api.amadeus.com/v1/reference-data/locations/cities"

load_dotenv()
# This class is responsible for talking to the Flight Search API.

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["AM_API_KEY"]
        self._api_secret = os.environ["AM_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=AM_TOKEN_ENDPOINT, headers=header, data=body)


        # print(response.json())
        # New bearer token. Typically expires in 1799 seconds (30min)
        # print(f"Your token is {response.json()['access_token']}")
        # print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_iata(self, city):
        header = {
            "Authorization": f"Bearer {self._token}"
        }

        params = {
            "keyword": city
        }
        response = requests.get(url=AM_GET_BY_CITY_ENDPOINT, headers=header, params=params)
        data = response.json()
        # print(f"data: {data}")

        iataCode = data["data"][0]["iataCode"]
        # print(iataCode)
        return iataCode


#
#
# # Amadeus
# AM_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token/"
# AM_API_KEY="Tsu88Cba1NwIn3aqmE6Heoc8JsL4xum9"
# AM_API_SECRET="gDJllCH3hsk8oFQi"
#
# parameters = {
#     "grant_type": "client_credentials",
#     "client_id": AM_API_KEY,
#     "client-secret": AM_API_SECRET,
# }
#
# headers = {
#     "content-type": "application/x-www-form-urlencoded"
# }
#
# # Get token
# response = requests.post(url=AM_TOKEN_ENDPOINT, json=parameters, headers=headers)
# print(response.text)