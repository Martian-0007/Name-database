# Import of modules
from datetime import datetime
import name_collect_functions as fx
import os
import json
import requests

# Variables
current_time = fx.CurTime()
file = "files/names-"+current_time+".json"
fx.flwrite("files/nof", "names-"+current_time+".json\n")
more = True
i = 1
url = "https://getpantry.cloud/apiv1/pantry/fbd15934-f1bf-4621-9086-e28c9e1c3b7c/basket/names"
headers = {'Content-Type': 'application/json'}


# The code itself
fx.flwrite(file, """{
    \"time\": \""""+current_time+"""\",
    \"names\": [\n""")

while(more): #WIP here
    # Write of the names into the file
    fx.flwrite(file, "        {\"id\": "+str(i)+", ")
    fx.getWriteNamejs(file)
    fx.flwrite(file, ", \"TimeOfArrival\": \""+fx.CurTime()+"\"")
    fx.flwrite(file, "}")
    print()
    morein = input("Ještě někdo? [Y/n]")
    if morein == "n":
        more = False
    elif morein == "Y":
        fx.flwrite(file, ",\n")
    else:
        raise ValueError(morein+' neni Y/n')
    print()
    i = i+1

fx.flwrite(file, "\n    ]\n}")

#API send
payload = open(file, 'rb').read()

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)