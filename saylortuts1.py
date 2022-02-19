'''#exam1
a = 3 
b = 4 
c = [a, b]
d = [c, a]
e = d+d
print(e[2])

#exam2
x = [2, 3, 4, 5, 'a', 'bee', 'c', 'dee']
x.append(3.14)
print(x)
x.extend(['m', 5.6, 'gee'])
x.pop()
x.pop(3)
print(x)

#exam3
x1= [ ]
for i in range(3):
    x1.append(i)
    x1.extend(x1)
print(x1)

#exam4
xvals = ['there', 'everywhere', 'herehere', 'zero', 'nowhere']
y = []
for i in xvals:
    y.append(i.find('ere'))
print(y)

#exam5
y1 = ['g', 'j', 'k', 'z', 'd', 'd', 'w' ]
y1.sort()
print(y1)

#exam6
x2= [2, 3, 4, 5, 'a', 'bee', 'c', 'dee']
print(x2[:])
print(x2[1:3])
print(x2[1:8:2])
print(x2[3:1:-1])
print(x2[2:len(x2)])
print(x2[2:])
print(x2[:3])
print(x2[-4:-1])
print(x2[-1])
print(x2[::2])

#exam7
x3 = [1, 2, 3, 4, 5, 6, 7, 8]
y2 = x3[::2]
z = y2.copy()
y2.append(x3[1::2])
z.extend(x3[1::2])
print(y2)
print(z)

#exam8
u = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p = u[-1:-5:-1]
o = u[::3]
for i in range(len(o)):
    print(p[i], o[i])


#Q11
inval = int(input('Put a number: '))
if inval>= 2 and inval <= 5:
    z = [1,3,5,7,9,2,4,6,8,10]
    for i in range(len(z)):
        if z[i] % inval == 0:
            print(f"{i} is divisible by the inval")
        else:
            print('You did not enter a number divisible by inval')      
else:
    print('You did not enter a number btn 2 and 5')

#Q12
z = ['lokose', 'lemi']
name = input(str('Put your name: '))
flag = 0
for i in z:
    if i == z:
        print(f'{name}, found it.')
        flag = 1
if (flag == 0):
    print(f'{name}, is not there')

#Q13
z = [1,2,3,4,5,6,7,8]
inval = float(input('Enter a number: '))
sum = 0
for i in z:
    if i > inval:
        sum+=i 
print(f'Sum of the numbers in the list greater than {inval}, =, {sum}')

#14
nstrings = 4
l = [ ]
message = input('type a message: ') 
for i in range(nstrings):
    l.append(input(message))
print(l)
'''