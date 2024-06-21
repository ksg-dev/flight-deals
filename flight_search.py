# This class is responsible for talking to the Flight Search API.
import os
from dotenv import load_dotenv
import requests

AM_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AM_GET_BY_CITY_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


load_dotenv()


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

        try:
            iataCode = response.json()["data"][0]["iataCode"]
            # print(iataCode)
        except IndexError:
            print(f"IndexError: No airport code found for {city}")
            return "N/A"
        except KeyError:
            print(f"KeyError: no airport code found for {city}")
            return "Not Found"
        return iataCode

    def get_flights(self, origin_iata, destination_iata, from_time, to_time):
        header = {
            "Authorization": f"Bearer {self._token}"
        }

        parameters = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "nonStop": "true",
            "currencyCode": "GBP",
            "adults": 1,
            "max": "10"
            }

        response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, headers=header, params=parameters)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body: ", response.text)
            return None

        return response.json()
