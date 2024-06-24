from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import date

search = FlightSearch()

a = ["NYC", "PAR", "DUB"]

today = date.today()
tom = today.replace(day=today.day + 1)
six_mon = today.replace(month=today.month + 6)

tomorrow = tom.isoformat()
six_months = six_mon.isoformat()

flights = search.get_flights(
    origin_iata="LON",
    destination_iata="DUB",
    from_time=tomorrow,
    to_time=six_months,
    is_direct=False
    )

# print(flights)
