import googlemaps
import datetime
import pandas as pd
from datetime import date
import webbrowser




client = googlemaps.Client(key = "AIzaSyBmsWtN7xBPyPjNQw_E6J9o8k5OKLG_WTA")

airport_list = pd.read_csv("majorAirports.csv", delimiter = ",").dropna()

test = airport_list[airport_list["IATA"].str.contains("BWI")]
#print(test["IATA"].tolist())


#this is a simple google map test
def get_distance(origin, destination, mode = "driving"):
    directions_result = client.distance_matrix(origin, destination, mode)
    origin_address = directions_result["origin_addresses"]
    destination_address = directions_result["destination_addresses"]
    distance = directions_result["rows"][0]["elements"][0]["distance"]["text"]
    duration = directions_result["rows"][0]["elements"][0]["duration"]["text"]
    return [origin_address, destination_address, distance, duration]



def get_nearest_places(query, location, radius = 2): #location = address
    address = get_distance(location, "white house")[0]
    geocode = client.geocode(address)[-1]["geometry"]["location"]
    places = client.places(query, location, radius)
    return places




def getAirportIATA(city):
    name = airport_list[airport_list["City"].str.contains(city.upper())]
    return name["IATA"].tolist()

def searchForFlights(city1, city2, date1, date2, passengers = 1):
    #current_date = date.today().strftime("%Y-%m-%d")
    #print(current_date)

    iata1 = getAirportIATA(city1)[0]
    iata2 = getAirportIATA(city2)[0]

    #quick_stats = get_distance(iata1, iata2)[0:2]
    webbrowser.open(f"https://www.southwest.com/air/booking/select.html?adultPassengersCount={passengers}&departureDate={date1}&returnDate={date2}&destinationAirportCode={iata2}&originationAirportCode={iata1}")
    #return quick_stats



