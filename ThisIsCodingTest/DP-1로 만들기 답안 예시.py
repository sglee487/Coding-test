import sys

sys.stdin = open("DP-1로 만들기.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    x = int(input())

    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 30001

    # 다이나막 프로그래밍 진행(보텀업)
    for i in range(2, x+1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i-1] + 1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        # 현재의 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    print(d[x])
    print(d)