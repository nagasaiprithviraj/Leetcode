def missingNumber(nums):
    nums.sort()

    temp = 0
    for i in range(len(nums) ):
        if temp == nums[i]:
            temp += 1
        else:
            return temp

if __name__ == '__main__':
    print(missingNumber([9,6,4,2,3,5,7,0,1]))
    print(missingNumber([3,0,1]))
    print(missingNumber([0]))

