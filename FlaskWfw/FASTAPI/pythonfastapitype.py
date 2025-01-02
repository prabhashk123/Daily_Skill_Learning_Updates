def add(firstname:str|list , lastname:str=None): #typing use kar sakte hai
    firstname.capitalize()
    # for item in firstname:
    #     item.capitalize()
    return firstname + " " + lastname
fname = "prabhash"
lname = "Kumar"

name=add(fname, lname)
print(name)
    