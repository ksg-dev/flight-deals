import os
import time
from datetime import date
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
TW_SID = os.environ["TWILIO_ACCOUNT_SID"]
TW_AUTH = os.environ["TWILIO_AUTH_TOKEN"]
TW_FROM = os.environ["FROM_NO"]
TW_TO = os.environ["TO_NO"]
client = Client(TW_SID, TW_AUTH)

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
    if flights["meta"]["count"] == 0:
        print(f"Checking indirect flights for {destination['city']}...")
        flights = search.get_flights(
            origin_iata=ORIGIN_IATA,
            destination_iata=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months,
            is_direct=False
        )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slow down requests to avoid api limit as suggested
    time.sleep(2)
    # try:
    #     if destination["lowestPrice"] > float(cheapest_flight.price):
    #         compose_msg = (f"We found a cheaper flight!\n"
    #                        f"Fly from {cheapest_flight.origin_airport} "
    #                        f"To {cheapest_flight.dest_airport} for only £{cheapest_flight.price}!\n"
    #                        f"Depart Date: {cheapest_flight.depart_date}\n"
    #                        f"Return Date: {cheapest_flight.return_date}\n"
    #                        f"Stops: {cheapest_flight.stops}")
    #
    #         message = client.messages.create(
    #             body=compose_msg,
    #             from_=TW_FROM,
    #             to=TW_TO
    #         )
    #         # print(message.body)
    # except TypeError:
    #     pass
    # except ValueError:
    #     pass


