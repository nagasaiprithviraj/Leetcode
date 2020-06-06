def threeSumClosest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)-2):
        l, r = i+1, len(nums) - 1
        while l < r:
            total = (nums[i] + nums[l] + nums[r])
            if abs(total-target) < abs(res-target):
                res = total
            if total < target:
                l += 1
            else:
                r -= 1
    return res

if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))
    print(threeSumClosest([0,1,2], 3))