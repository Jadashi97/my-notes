
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

