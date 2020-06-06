def reorderLogFiles(logs):
    letter_logs = []
    digit_logs = []
    for i in logs:
        if i.split()[1].isdigit():
            digit_logs.append(i)
        else:
            letter_logs.append(i.split())
    print(letter_logs)
    letter_logs.sort(key=lambda x: x[0])
    print(letter_logs)
    letter_logs.sort(key=lambda x: x[1:])
    print(letter_logs)
    for i in range(len(letter_logs)):
        letter_logs[i] = " ".join(letter_logs[i])
    return letter_logs + digit_logs


if __name__ == '__main__':
    # print(reorderLogFiles_1(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print(reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
