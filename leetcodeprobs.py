'''
#HW1
nums = [2,7,11,15]
target = 9
class solution(object):
    def twosum(self, nums, target):
        nums_indx = { }
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums_indx:
                return [i, nums_indx[diff]]
            nums_indx[nums[1]] = i

#data structures. Q1
nums = [2,3,1,2,3]
#class Solution(object):
def containsDuplicate(nums):
    S = { }
    for i in nums:
        if i in S:
            return True
        else:
            S[i] = 1
    return False

print(containsDuplicate(nums))

#reversing strings
#1
s = [ "h","e","l","l","o"]
s.reverse()
print(s)

#2
s = ["H","a","n","n","a","h"]
s.reverse()
print(s)

#3
x = [-2^32, 2^32, -1]
print(x[-1:-1])

#working on classes and functions
#Qa
class Car:
    def __init__(self, speed, color):
        self.speed = speed 
        self.color = color
        print(speed)
        print(color)
        print('the __init__ is called')

ford = Car(200, 'red')
honda = Car(180, 'purple')
audi = Car(230, 'maroon')

class Area:
    def __init__(self,height, width):
        print(height)
        print(width)
        self.height = height
        self.width = width
rect1 = Area(20,40)
rect2 = Area(30, 50)
print(rect1.height * rect1.width)
print(rect2.height * rect2.width)
'''
# not sure consult
List = [1,1,2]

class Solution:
     def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[k] == nums[i]:
                k.pop()
            else:
                nums[k+1] = nums[i]
        return k+1 
'''
# 1st unique character string
s = "leetcode"

def find_chr(s):
    for e in s:
        if e == 1:
            return s.index()
        else:
            -1
print(find_chr(s))
'''