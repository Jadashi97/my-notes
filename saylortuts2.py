#working on regular expressions

import re
'''
#1
personList = ['Julia', 'Francis Drake', 'Michael Mason', 'jennifer Johnson', 'John Williams', 'Susanne Walker', 'Kermit the Frog', 'Dr.Melissa Franklin', 'Papa John', ' Walter John Miller', 'Franklin Michael Robertson', 'Richard Robertson', 'Erik D. White', 'Vincent van Gogh', 'Dr. Dr. Matthew Malone', 'Rebecca Clark']

pattern = 'John'

for person in personList:
    if re.match(pattern, person):
        print(person)
     
compiled_pattern = re.compile(pattern)
for person in personList:
    if compiled_pattern.match(person):
        print(person)
'''
#2
list = ['adfac', 'babba', 'cbaca', ' fbaceeef']
pattern = 'a.*b'
for i in list:
    if re.search(pattern, list):
        print(i)