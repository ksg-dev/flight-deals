# This class is responsible for talking to the Flight Search API.

class FlightSearch:
    def __init__(self):
        pass
        # self.city = city
        # self.iatacode = self.get_iata(self.city)

    def get_iata(self, city):
        return ("TESTING")


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