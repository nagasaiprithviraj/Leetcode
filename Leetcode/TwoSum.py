"""Here two for loops are used Time complexity is O(n^2) and space complexity is O(1) as you used one list"""
# Brute Force Algorithm
def twoSum_1(nums, target):
    for i in range(len(nums)):
        for j in range((i+1), len(nums)):
            if (nums[j] == (target - nums[i])):
                return [i, j]

"""Time Complexity O(n) as other for loop is look into hash table where O(n) and space complexity is O(n)"""
# Two-pass Hash
def twoSum_2(nums, target):
    thisdict = {}
    for i in range(len(nums)):
        thisdict[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in thisdict:
            return [i, thisdict[complement]]

# One-pass Hash
def twoSum_3(nums, target):
    thisdict = {}
    for i in range(len(nums)):
        thisdict[nums[i]] = i
        complement = target - nums[i]
        if complement in thisdict:
            return [i, thisdict[complement]]


if __name__ == '__main__':
    print(twoSum_1([2,11,7,15], 9))
    print(twoSum_2([2,11,5,15,7], 9))
    print(twoSum_3([2,11,5,15,7], 9))
