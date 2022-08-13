# Import of modules
from datetime import datetime
import name_collect_functions as fx
import os
import json
import requests

# Variables
now = datetime.now()
current_time = now.strftime("%d-%m-%Y_%H.%M.%S")
file = "files/names-"+current_time+".json"
fx.flwrite("files/nof", "names-"+current_time+".json\n")
more = True
i = 1
url = "https://getpantry.cloud/apiv1/pantry/fbd15934-f1bf-4621-9086-e28c9e1c3b7c/basket/names-"+current_time+".json"
headers = {'Content-Type': 'application/json'}


# The code itself
fx.flwrite(file, """{
    \"names\": [\n""")

while(more): #WIP here
    # Write of the names into the file
    fx.flwrite(file, "        {\"id\": "+str(i)+", ")
    fx.getWriteNamejs(file)
    fx.flwrite(file, "}")
    print()
    morein = input("Ještě někdo? [Y/n]")
    if morein != "Y":
        more = False
    else:
        fx.flwrite(file, ",\n")
    print()
    i = i+1

fx.flwrite(file, "\n    ]\n}")

# Print out the file full of names
#f = open(file, "r")
#print("\nVýpis účastníků:")
#print("\n"+f.read())
#f.close

#API send
payload = open(file, 'rb').read()

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)