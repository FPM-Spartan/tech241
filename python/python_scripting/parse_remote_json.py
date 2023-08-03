# parse remote json

import urllib.request
import json

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url: # take what's in there and stick it in a variable called url
    data = json.load(url)
    print(data)
    print(type(data))



