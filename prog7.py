import re
def find_last_and_initial(in_str):
    found = re.search(r'^\w+,?\s*[A-Z]$',in_str)
    if found:
        print("yes")
    else:
        print("No")
        

find_last_and_initial('Smith, J')
find_last_and_initial('M Cano')
find_last_and_initial('Nguyen C')
