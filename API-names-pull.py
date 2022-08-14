# Imports
import requests
import json
from datetime import datetime

# Variables
url = "https://getpantry.cloud/apiv1/pantry/fbd15934-f1bf-4621-9086-e28c9e1c3b7c/basket/names"
now = datetime.now()
current_time = now.strftime("%d-%m-%Y_%H.%M.%S")



# Getting the response
response = requests.get(url)

response = response.json()

# Wriing into a file
JsonResponse = json.dumps(response)
filename = open("files/response"+current_time+".json", "a")
filename.write(JsonResponse)
filename.close()