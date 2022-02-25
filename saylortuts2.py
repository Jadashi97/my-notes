#working on regular expressions
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

#5 & 6
list = ['adfac', 'babba', 'cbaca', ' fbaceeef']
pattern = 'a.*b'
for i in list:
    if re.match(pattern, i):
        print(i)

def re_pattern(text, pattern):
    print("  '{}'".format(text))
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        substr_match = text[s:e]
        dot_prefix = '.'* s
        print("  {}'{}'".format(dot_prefix, substr_match))
    print()
    return

#7 re_pattern('Michael is in Los Angeles with his family', '[A-Z][a-z]+')
#8 re_pattern('cddccdddc', 'cd?')
#9 re_pattern('cdcddccddddc', 'cd{2,3}')

#10
f = open(' str_data.txt', 'r')
for str_match in re.finditer('a((a+)|(b+))', f.read()):
    print(str_match.start(), str_match.end())
f.close()

#10 not sure what to do here.
str_data = 'abbaabbba'

for i in re.finditer('a((a+)|(b+))', str_data):
    print(str_data.start(), str_data.end())

#11 not sure 
import re
kose = "ccdadababdd"

def locate(kose):
    for kose in 'a.*b':
        regex = re.compile(kose)
        if regex.search(kose) != None:
            return True
        return False

print(locate(kose))

#12
import re
nums = 'gggabcabcabceeee'
def findnum(nums):
    for i in nums:
        if re.search('[a-b]d.', nums):
            return True
        else:
            return False
print(findnum(nums))
'''
