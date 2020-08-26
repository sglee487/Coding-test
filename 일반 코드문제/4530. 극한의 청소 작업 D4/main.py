import sys

sys.stdin = open("sample_input2.txt", "r")

def solve(n):
    # 9진법을 다루는 것 같다....
    r = 0
    i = 0
    while n // (10 ** i) > 0:
        d = n % (10 ** (i+1)) // (10 ** i)
        # print("n // (10 ** i): {}, d: {}".format(n // (10 ** i),d))
        if d > 4: d -= 1
        r += (9**i) * d
        i += 1
    return r

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    A, B = map(int, input().split())
    result1 = solve(abs(A))
    result2 = solve(abs(B))
    if (A > 0) or (B < 0):
        result = abs(result1-result2)
    else:
        result = abs(result1+result2) - 1

    print("#{}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
