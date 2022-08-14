# Import of modules
from datetime import datetime
from distutils.log import info
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
now = fx.CurTime()
ppl = []


while(more):
    personinfo = {}
    personinfo["no."] = i
    personinfo["jmeno"] = input("Jak se jmenujes?\n")
    personinfo["TimeOfArrival"] = now
    print(personinfo)
    ppl.append(personinfo)
    finaljs = json.dumps(ppl, ensure_ascii=False, indent=2)
    print()

    morein = input("Ještě někdo? [Y/n]")
    if morein == "n":
        more = False
        with open('files/data.json', 'w') as soubor:
            print(finaljs, file=soubor)
    elif morein == "Y":
        more = True
    else:
        raise ValueError(morein+' neni Y/n')
    print()
    i = i+1


#API send
payload = open(file, 'rb').read()

#response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)