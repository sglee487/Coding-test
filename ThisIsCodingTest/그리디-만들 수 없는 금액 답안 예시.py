import sys

sys.stdin = open("그리디-만들 수 없는 금액.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # https://github.com/ndb796/python-for-coding-test/blob/master/11/4.py
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    target = 1
    for x in data:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < x:
            break
        target += x

    # 만들 수 없는 금액 출력
    print(target)