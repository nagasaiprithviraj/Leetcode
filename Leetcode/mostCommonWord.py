def mostCommonWord(paragraph, banned):
    this_dict = {}
    paragraph = paragraph.lower()
    for i in paragraph:
        if i in "!?',;.":
            paragraph = paragraph.replace(i, " ")
    paragraph = paragraph.split()
    # print(paragraph)
    for i in range(len(paragraph)):
        if paragraph[i] not in this_dict:
            this_dict[paragraph[i]] = 1
        else:
            this_dict[paragraph[i]] += 1
    this_dict = {k: v for k, v in sorted(this_dict.items(), key=lambda item: item[1], reverse=True)}
    # print(this_dict)
    for i in this_dict:
        if i in banned:
            continue
        else:
            return i

def mostCommonWord_1(paragraph, banned):
    paragraph = paragraph.lower()
    for i in paragraph:
        if i in "!?',;.":
            paragraph = paragraph.replace(i, " ")
    paragraph = paragraph.split()
    max_count = 0
    Res = ''
    for i in paragraph:
        if i not in banned:
            if paragraph.count(i) > max_count:
                max_count = paragraph.count(i)
                Res = i
    return Res

if __name__ == '__main__':
    # print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
    print(mostCommonWord_1("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
