import sys

sys.stdin = open("input.txt", "r")

def dfs(n,value,used_list):
    global result_product
    if n == N:
        if result_product < value:
            result_product = value
        return

    if value < result_product:
        return

    for i in range(N):
        if i in used_list: continue
        used_list.append(i)
        dfs(n+1,value * (Percents[n][i]/100),used_list)
        used_list.remove(i)

    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    Percents = []
    for _ in range(N):
        Percents.append(list(map(int, input().split())))

    print(Percents)

    result_product = 0.000000

    dfs(0,1,[])

    print(result_product)

    print("#{}".format(test_case),"{:6f}".format(result_product*100))
    # ///////////////////////////////////////////////////////////////////////////////////
