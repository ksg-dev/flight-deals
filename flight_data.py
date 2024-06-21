# This class is responsible for structuring the flight data.
import requests
from datetime import date
from flight_search import FlightSearch




class FlightData:
    def __init__(self, price, origin_airport, dest_airport, depart_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.dest_airport = dest_airport
        self.depart_date = depart_date
        self.return_date = return_date



        """
        post_params = {
            "currencyCode": "USD",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": "LON",
                    "destinationLocationCode": destination_iata,
                    "departureDateTimeRange": {
                        "date": tomorrow,
                        # "dateWindow": "P180D"
                    }
                }
              ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                }
              ],
            "sources": ["GDS"]
            }

        response = requests.post(url=FLIGHT_OFFERS_ENDPOINT, headers=header, params=post_params)
        data = response.json()
        print(response.status_code)
        print(data)
        """