def getWriteName(filename):
    #Gets the name of a person and writes it into a file
    f = open(filename, "a")
    name = input("Jak se jmenuješ?\n")
    f.write(name+"\n")
    f.close()