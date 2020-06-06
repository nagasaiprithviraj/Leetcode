def threeSum(nums):
    nums.sort()
    value = 0
    Res = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = nums[i]
        L = i + 1
        R = len(nums)-1
        while L < R:

            Total_sum = target+nums[L]+nums[R]
            if Total_sum < value:
                L += 1
            elif Total_sum > value:
                R -= 1
            elif Total_sum == value:
                Res.append([target, nums[L], nums[R]])
                while L < R and nums[L] == nums[L+1]:
                    L += 1
                while L < R and nums[R] == nums[R-1]:
                    R -= 1
                L += 1
                R -= 1
    return Res

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([0,0,0,0]))
