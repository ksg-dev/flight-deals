# This class is responsible for structuring the flight data.
import requests
from datetime import date
from flight_search import FlightSearch


FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightData:
    def __init__(self):
        self.price = 0
        self.departure_code = "LON"
        search = FlightSearch()
        self._token = search._get_new_token()

    def get_flights(self, destination_iata):
        today = date.today()
        tom = today.replace(day=today.day + 1)
        tomorrow = tom.isoformat()

        header = {
            "X-HTTP-Method-Override": "GET",
            "Authorization": f"Bearer {self._token}"
        }

        o_destinations = {
            "originLocationCode": self.departure_code,
            "destinationLocationCode": destination_iata,
            "departureDateTimeRange": {
                "date": tomorrow,
            }
        }

        body = {
            "currencyCode": "USD",
            "originDestinations": o_destinations,
            "travelers": {
                "id": "1",
                "travelerType": "ADULT"
                },
            "sources": "GDS"
            }

        response = requests.post(url=FLIGHT_OFFERS_ENDPOINT, headers=header, data=body)
        print(response.status_code)
        data = response.json()
        print(data)