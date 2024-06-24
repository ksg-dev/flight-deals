# This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, price, origin_airport, dest_airport, depart_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.dest_airport = dest_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    """
      Parses flight data received from the Amadeus API to identify the cheapest flight option among
      multiple entries.

      Args:
          data (dict): The JSON data containing flight information returned by the API.

      Returns:
          FlightData: An instance of the FlightData class representing the cheapest flight found,
          or a FlightData instance where all fields are 'NA' if no valid flight data is available.

      This function initially checks if the data contains valid flight entries. If no valid data is found,
      it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
      flight in the list is the cheapest. It then iterates through all available flights in the data, updating
       the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
       FlightData object with the details of the most affordable flight.
      """

    # Handle empty data or api rate limit exceeded
    if data is None or not data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Data from first flight in json
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    depart_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    num_stops = first_flight["itineraries"][0]["segments"][0]["numberOfStops"]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, depart_date, return_date, num_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            depart_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            num_stops = first_flight["itineraries"][0]["segments"][0]["numberOfStops"]
            print(f"Lowest price to {destination} is £{lowest_price} with {num_stops} stops")

    return cheapest_flight

