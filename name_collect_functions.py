def getWriteName(filename):
    #Gets the name of a person and writes it into a file
    f = open(filename, "a")
    name = input("Jak se jmenuješ?\n")
    f.write(name+"\n")
    f.close()

def flwrite(filename, content):
    # Utility for writing into a file
    f = open(filename, "a")
    f.write(content)
    f.close()

def getWriteNamejs(filename):
    #Gets the name of a person and writes it into a file
    import json
    f = open(filename, "a")
    name = input("Jak se jmenuješ?\n")
    name = name.json()
    jsname = json.dumps(name)
    f.write(jsname+"\n")
    f.close()

def flwritejs(filename, content):
    # Utility for writing into a file
    import json
    f = open(filename, "a")
    content = content.json()
    jscontent = json.dumps(content)
    f.write(jscontent)
    f.close()