#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

sheet = DataManager()
sheet_data = sheet.get_data()
# pprint(sheet_data)

search = FlightSearch()
# cities = sheet_data[0]["city"]
# ct = [value for (key, value) in sheet_data.items()]
# print(cities)
# print(ct)

for row in sheet_data:
    city = row["city"]
    row_id = row["id"]
    if row["iataCode"] == "":
        row["iataCode"] = search.get_iata(city)
    update = {
        "price": {
            "city": city,
            "iataCode": row["iataCode"],
            "lowestPrice": row["lowestPrice"]
        }
    }
    sheet.update_data(row_id, update)
print(sheet_data)



#
# for entry in range(len(sheet_data)):
#     city = sheet_data[entry]["city"]
#     # id = sheet_data[entry]["id"]
#     # low = sheet_data[entry]["lowestPrice"]
#     iata = sheet_data[entry]["iataCode"]
#     # print(city)
#     # print(id)
#     # print(sheet_data)
#     if iata == "":
#         iata = search.get_iata(city)

    # sheet.update_data(row_id=id, json=sheet_data[entry])
    # print(sheet_data[entry])
# print(sheet_data)
    # sheet.update_data(row_id=id, json=sheet_data)






