import sys

sys.stdin = open("그리디-모험가 길드.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _ = input()
    people = list(map(int, input().split()))
    people.sort(reverse=True)

    result = 0
    start = 0
    while start < len(people):
        cap = people[start]
        if start + cap < len(people):
            start += cap
            result += 1
        else:
            start += 1

    print(result)