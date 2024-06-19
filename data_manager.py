import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, city, iatacode, lowestprice, row_id):
        self.endpoint = "https://api.sheety.co/e938eee05710f2891def63457d60664d/flightDeals/prices"
        self.city = city
        self.iatacode = iatacode
        self.lowestprice = lowestprice
        self.id = row_id
        self.entry = {
            "price": {
                "city": self.city,
                "iataCode": self.iatacode,
                "lowestPrice": self.lowestprice,
                "id": self.id
            }
        }

    def get_data(self):
        response = requests.get(url=self.endpoint)
        data = response.json()
        # print(data)
        prices = data["prices"]
        return prices

    def update_data(self, row_id, update_json):
        update_json = {
            "price": {
                "city": city,

            }
        }
        requests.put(url=f"{self.endpoint}/{row_id}", json=json)