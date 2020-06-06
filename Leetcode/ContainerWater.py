def maxArea(lst):
    first = 0
    last = len(lst)-1
    max_area = 0

    while first < last:
        max_area = max(max_area, (min(lst[first], lst[last]) * (last - first)))

        if lst[first] < lst[last]:
            first += 1
        else:
            last -= 1
    return max_area

if __name__ == '__main__':
    # print(maxArea([1,8,6,2,5,4,8,3,7]))
    print(maxArea([1,9,9,1]))

    # maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
