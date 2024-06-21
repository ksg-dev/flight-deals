import time
from datetime import date
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# ================ SET UP FLIGHT SEARCH ================ #
sheet = DataManager()
sheet_data = sheet.get_data()

search = FlightSearch()

ORIGIN_IATA = "LON"


# ================ UPDATE IATA CODES IN SHEET ================ #
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = search.get_iata(row["city"])
        # Adding sleep to avoid rate limits as suggested
        time.sleep(2)

sheet.destination_data = sheet_data
sheet.update_data()

# ================ SEARCH FOR FLIGHTS ================ #

today = date.today()
tom = today.replace(day=today.day + 1)
six_mon = today.replace(month=today.month + 6)

tomorrow = tom.isoformat()
six_months = six_mon.isoformat()

# print(tomorrow)
# print(six_months)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = search.get_flights(
        origin_iata=ORIGIN_IATA,
        destination_iata=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slow down requests to avoid api limit as suggested
    time.sleep(2)



