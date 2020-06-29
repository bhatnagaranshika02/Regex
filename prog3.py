import re
def finder(pattern,word):
    found = re.search(pattern,word)
    if found:
        print("yes")
    else:
        print("No")
finder(r'e.t' , 'better')
finder(r'e.t','either')
finder(r'e.t','best')
