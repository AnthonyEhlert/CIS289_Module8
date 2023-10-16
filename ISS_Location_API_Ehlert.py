"""
Program Name: IIS_Location_Ehlert.py
Author: Tony Ehlert
Date: 10/11/2023

Program Description: This program utilizes an open API to get information about the International Space Station.
Using the data from the API this program finds the current location of the ISS and the current astronauts currently
residing on the ISS and prints all that info to the console.
"""
import requests

#### Use the API documentation at http://open-notify.org/Open-Notify-API/ISS-Location-Now/ to build your API request

#### Find out the current location of the ISS and print it to the console
cur_loc_url = "http://api.open-notify.org/iss-now.json"
request = requests.get(cur_loc_url)
# print(type(request.json()))
# print(json.dumps(request.json(), indent=4, sort_keys=True))
print("The current position of the ISS is:")
print(f"Latitude: {request.json()['iss_position']['latitude']}")
print(f"Longitude: {request.json()['iss_position']['longitude']}")
print()

#### Find out the names of the current residents of the ISS and print it to the console
cur_residents_url = "http://api.open-notify.org/astros.json"
request = requests.get(cur_residents_url)
# print(json.dumps(request.json(), indent=4, sort_keys=True))
print("The names of current residents of the ISS are:")
for person in request.json()['people']:
    print(person['name'])
print()

#### Outputs should be formatted to answer the questions.  Needs to be beyond just printing the json to the console.
