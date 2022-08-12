# Import of mine module
import name_collect_functions as fx

# Variables
GN = input("Kolik je účastníků?\n")
GN = int(GN)

file = "names.txt"


# The code itself
for i in range(GN):
    fx.getWriteName(file)