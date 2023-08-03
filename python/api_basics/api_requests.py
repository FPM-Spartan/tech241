"""
REQUESTS
"""

import requests
import json

# get request
# 90% of the time people use APIs for get requests

post_code_req = requests.get("https://api.postcodes.io/postcodes/fk81ny")

# print(post_code_req) # <Response [200]>
# print(type(post_code_req)) #requests.models.response
# print(post_code_req.status_code) # 200
# print(type(post_code_req.status_code)) #int
# print(post_code_req.content) # returns contents of the uri, as bytes
# print(type(post_code_req.content)) # <bytes>
print(post_code_req.json()) # returns contents of the uri as python dict
print(type(post_code_req.json())) # <dict>

# post request - sending data to the API

json_body = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

# the posts codes are being parsed into json

headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())
print(headers)
print(json_body)

# pokemon api

# pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon")
# print(pokemon_req.json())

# BBC webpages

# bbc_request = requests.get("https://www.bbc.co.uk")
# print(bbc_request.content) # nb you can't just use .json for a webpage. you have to use .content
