import re
def find_boundary(in_str):
    found1 = re.search(r'\bmet',in_str)
    found2 = re.search(r'\ing\b',in_str)
    found3 = re.search(r'\bhat\b',in_str)
    if found1:
        print("yes")
    if found2:
        print("yes")
    if found3:
        print("yes")

in_str = input('Enter one of the preceding sentences:')
find_boundary(in_str)
        
