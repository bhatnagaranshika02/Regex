import re
def find_ssn(strr):
    found = re.search(r'\d\d\d-\d\d-\d\d\d\d',strr)
    if found:
        print("Yes")
    else:
        print("No")

find_ssn('301-44-4567')
find_ssn('2-33-345')
