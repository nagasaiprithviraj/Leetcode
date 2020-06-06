# def productExceptSelf(nums):
#     Cn = []
#     for i in range(len(nums)):
#         res = 1
#         for j in range(len(nums)):
#             if j == i:
#                 continue
#             else:
#                 res *= nums[j]
#         Cn.append(res)
#     return Cn

def productExceptSelf(nums):
    Left, Right = [1]*len(nums), []
    for i in range(len(nums)):
        Left.append(1)
        Right.append(1)
    for i in range(1, len(nums)):
        Left[i] = Left[i-1]*nums[i-1]
    for i in reversed(range(len(nums)-1)):
        Right[i] = Right[i+1]*nums[i+1]
    Res = []
    for i in range(len(Left)):
        Res.append(Left[i] * Right[i])
    return Res

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))