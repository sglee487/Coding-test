import sys

sys.stdin = open("구현-럭키 스트레이트.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S = input()
    left, right = 0, 0
    for c in S[:len(S)//2]:
        left += int(c)
    for c in S[len(S)//2:]:
        right += int(c)
    if left == right:
        print("LUCKY")
    else:
        print("READY")
