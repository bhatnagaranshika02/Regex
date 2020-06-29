import re
def finder(pattern,word):
    found = re.search(pattern,word)
    if found:
        print('yes')
    else:
        print("No")

finder(r'b[aeiou]t','bat')
finder(r'b[aeiou]t','rabbit')
