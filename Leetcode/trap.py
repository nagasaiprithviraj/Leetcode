def trap(height):
    left_max, right_max = 0, 0
    L, R = 0, len(height)-1
    res = 0

    while L < R:
        left_max = max(left_max, height[L])
        right_max = max(right_max, height[R])
        if left_max <= right_max:
            res += (left_max - height[L])
            L += 1
        else:
            res += (right_max-height[R])
            R -= 1
    return res

if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))