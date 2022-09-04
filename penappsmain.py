import googlemaps
import datetime
from gmapsearch import *

def checkFlight():
    origin_city = input("Enter an origin city: ")
    destination_city = input("Enter a destination_city: ")
    origin_date = input("Enter the date you'll leave(yyyy-mm-dd): ")
    destination_date = input("Enter the date you'll come back (yyyy-mm-dd) :")
    passenger_count = int(input("How many passengers will be go on this trip?"))
    searchForFlights(origin_city, destination_city, origin_date, destination_date, passenger_count)

    
def get_two_distances():
    start = input("Enter a location: ")
    destination = input("Enter a destination: ")
    return get_distance(start, destination)

def getOptions():
    print("1. Check a flight")
    print("2. Get distance between two locations")
    choice = int(input())
    if choice != 1 and choice != 2:
        print("Invalid; Please try again")
        getOptions()
    else:
        if choice == 1:
            try:
                checkFlight()
            except IndexError:
                print("One of the locations do not exist!")
                getOptions()
        else:
            print(get_two_distances())

def greeting():
    print("How may I help you today")
    getOptions()

def main():
    print("Hello There! I am your personal text based assistant. ")
    cont = True
    while cont:
        greeting()
        question = input("Would you like to try again? Y/N")
        if question.upper() != "Y":
            cont = False
        
        print("Have a nice day!")



if __name__ == "__main__":
    main()
