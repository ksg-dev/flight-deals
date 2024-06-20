import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

SHEETY_ENDPOINT="https://api.sheety.co/e938eee05710f2891def63457d60664d/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SH_USER"]
        self._password = os.environ["SH_PASSWORD"]
        self._auth = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._auth)
        data = response.json()
        # print(f"data: {data}")
        self.destination_data = data["prices"]
        return self.destination_data

    def add_data(self):
        add_row = requests.post(url=SHEETY_ENDPOINT, auth=self._auth)

    def update_data(self):
        for row in self.destination_data:
            update = {
                "price": {
                    "iataCode": row["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{row['id']}",
                json=update,
                auth=self._auth
            )