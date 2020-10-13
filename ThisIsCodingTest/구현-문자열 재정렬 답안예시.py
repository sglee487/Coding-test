import sys

sys.stdin = open("구현-문자열 재정렬.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    data = input()
    result = []
    value = 0

    # https://soooprmx.com/archives/10159
    for x in data:
        if x.isalpha():
            result.append(x)
        else:
            value += int(x)

    result.sort()

    if value != 0:
        result.append(str(value))

    print(''.join(result))