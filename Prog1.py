import re
word = input("Enter a string: ")
found = re.search(r'e',word)
if found:
    print('yes')
else:
    print('No')
