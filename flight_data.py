# This class is responsible for structuring the flight data.
import requests
from datetime import datetime


FLIGHT_OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightData:
    def __init__(self):
        self.price = 0
        self.departure_code = "LON"

    def get_flights(self):
        today = datetime.now()


        header = {
            "X-HTTP-Method-Override": "GET",
        }

        o_destinations = {
            "originLocationCode": self.departure_code,
            "destinationLocationCode": "DUB",
            "departureDateTimeRange": {
                "date":
            }
        }

        parameters = {
            "currencyCode": "GBP",
            "originDestinations":
        }