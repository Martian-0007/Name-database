def getWriteName(filename):
    #Gets the name of a person and writes it into a file
    f = open(filename, "a")
    name = input("Jak se jmenuješ?\n")
    f.write(name+"\n")
    f.close()
    return()

def flwrite(filename, content):
    # Utility for writing into a file
    f = open(filename, "a")
    f.write(content)
    f.close()
    return()

def getWriteNamejs(filename):
    #Gets the name of a person and writes it into a file
    import json
    f = open(filename, "a")
    name = input("Jak se jmenuješ?\n")
    f.write("\"name\": \""+name+"\"")
    f.close()
    return()

def flwritejs(filename, contentname, content):
    # Utility for writing into a file
    import json
    f = open(filename, "a")
    f.write("{"+"\""+contentname+"\": "+content+"},\n")
    f.close()
    return()

def CurTime():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y_%H-%M-%S")
    return(current_time)