"""
Program Name: Access_API_Ehlet.py
Author: Tony Ehlert
Date: 10/11/2023

Program Description: This program accesses an API for the popular MMO video game Final Fantasy XIV.  It makes a call
to the API from within Python that requests data with specific parameters.  After that it prints the downloaded data
to the console.
"""
import requests
import json

#### Use either the API you researched, one your fellow students researched, or a completely different one
#### Make an API call from within Python requesting data with specified parameters
# create variable storing base url needed
base_url_api = "https://xivapi.com"

# create list of categories that can be searched
search_cat_list = ["character", "freecompany", "linkshell"]

# create variable to store name to be searched for
character_name = "enzinger eagle"

# send request to API to search for name
response = requests.get(f"{base_url_api}/{search_cat_list[0]}/search?name={character_name}")
jsoned_response = response.json()
# print(jsoned_response)

# create character_id variable and extract character ID from jsoned_response
character_id = None
for item in jsoned_response['Results']:
    for key, value in dict.items(item):
        if str(value).lower() == character_name.lower():
            character_id = item['ID']
            break

# make new call to API using character_id to pull character profile info
char_prof_response = requests.get(f"{base_url_api}/{search_cat_list[0]}/{character_id}")

#### Output the downloaded data to the console
print(json.dumps(char_prof_response.json(), sort_keys=True, indent=4))
