import re
def find_eat(word):
    found = re.search(r'eat',word)
    if found:
        print(word, 'contains the letters "eat".')
    else:
        print(word, 'does not contain the letters "eat".')


find_eat('heater')
find_eat('treat')
find_eat('easy')
find_eat('metal')
