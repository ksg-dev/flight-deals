import requests
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()


sheet = DataManager()
sheet_data = sheet.get_data()
# pprint(sheet_data)

search = FlightSearch()

# Check if row has value in IATA code, if not, update w flight search
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = search.get_iata(row["city"])
sheet.destination_data = sheet_data
sheet.update_data()




