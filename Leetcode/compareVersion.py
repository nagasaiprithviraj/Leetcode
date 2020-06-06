def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    max_length = max(len(version1), len(version2))
    min_length = min(len(version1), len(version2))
    # if min_length == len(version1):
    #     minimum = version1
    # else:
    #     minimum = version2
    #
    # for i in range(min_length, max_length):
    #     minimum.append("0")

    for i in range(max_length):
        if int(version1[i]) < int(version2[i]):
            return -1
        elif int(version1[i]) > int(version2[i]):
            return 1
        # elif (i == max_length-1) and (int(version1[i]) == int(version2[i])):
        #     return 0
    return 0



if __name__ == '__main__':
    print(compareVersion("1", "1"))
