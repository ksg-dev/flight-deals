import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/e938eee05710f2891def63457d60664d/flightDeals/prices"
        # self.data = {
        #     "price": {
        #         "city": city,
        #         "iataCode": iata,
        #         "lowestPrice": price
        #     }
        # }

    def get_data(self):
        response = requests.get(url=self.endpoint)
        data = response.json()
        # print(f"data: {data}")
        prices = data["prices"]
        return prices

    def add_data(self):
        add_row = requests.post(url=self.endpoint, )

    def update_data(self, row_id, update_json):
        # update_json = {
        #     "price": {
        #         "city": city,
        #         "iataCode": iata,
        #         "lowestPrice": lowest_price
        #
        #     }
        # }
        requests.put(url=f"{self.endpoint}/{row_id}", json=update_json)