# Import of modules
import name_collect_functions as fx
import os

# Variables
GN = input("Kolik je účastníků?\n")
GN = int(GN)

file = "names.txt"

#deleting the old file, if there is one
try:
    os.remove(file)
except FileNotFoundError:
    print("-")

# The code itself
# Getting some space after the Guest number question
print()

for i in range(GN):
    # Write of the names into the file
    fx.flwrite(file, str(i+1)+"# ")
    fx.getWriteName(file)
    print()

# Print out the file full of names
f = open(file, "r")
print("\nVýpis účastníků:")
print("\n"+f.read())