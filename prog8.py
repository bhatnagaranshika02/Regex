import re
def valid_postcode(in_str):
    found = re.search(r'^[A-Z]\d[A-Z]\s+\d[A-Z]\d$',in_str,flags=re.I)
    if found:
        print("yes")
    else:
        print("nO")

valid_postcode('A5B 6R9')
valid_postcode('c7H 8j2')

