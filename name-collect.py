# Import of modules
from datetime import datetime
import name_collect_functions as fx
import os
import json

# Variables
now = datetime.now()
current_time = now.strftime("%d-%m-%Y_%H.%M.%S")
file = "C://Users/marta/Documents/GitHub/Name-database/files/names-"+current_time+".json"
more = True
i = 1

# The code itself
while(more): #WIP here
    # Write of the names into the file
    fx.flwrite(file, str(i)+"# ")
    fx.getWriteName(file)
    print()
    morein = input("Ještě někdo? [Y/n]")
    if morein != "Y":
        more = False
#    if morein == "n":
#        more = False
#    elif morein != "Y":
#        print("Tato odpověď nebyla v nabídce - konec")
#        quit()
    print()
    i = i+1

# Print out the file full of names
f = open(file, "r")
print("\nVýpis účastníků:")
print("\n"+f.read())
f.close