import time
from datetime import date
from data_manager import DataManager
from flight_search import FlightSearch
# from flight_data import find_cheapest_flight

# ================ SET UP FLIGHT SEARCH ================ #
# sheet = DataManager()
# sheet_data = sheet.get_data()

# search = FlightSearch()

ORIGIN_IATA = "LON"


# ================ UPDATE IATA CODES IN SHEET ================ #
# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = search.get_iata(row["city"])
#         # Adding sleep to avoid rate limits as suggested
#         time.sleep(2)
#
# sheet.destination_data = sheet_data
# sheet.update_data()

# ================ SEARCH FOR FLIGHTS ================ #

today = date.today().isoformat()
print(today)




