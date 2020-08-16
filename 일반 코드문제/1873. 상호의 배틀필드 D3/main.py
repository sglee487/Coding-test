import sys

sys.stdin = open("input2.txt", "r")

def shoot(p,d):
    return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    H, W = map(int, input().split())
    Map = []
    for _ in range(H):
        Map.append(list(input()))
    _ = input()
    inpl = list(input())

    print(*Map,sep='\n')
    print(inpl)

    tank = (-1,-1)
    for r in range(H):
        for c in range(W):
            if Map[r][c] == '<' or Map[r][c] == '>' or Map[r][c] == '^' or Map[r][c] == 'v':
                tank = (r,c)
                break
        if tank != (-1,-1): break

    for inp in inpl:
        if inp == 'S':
            pass
        if inp == 'U':
            pass
        if inp == 'D':
            pass
        if inp == 'L':
            pass
        if inp == 'R':
            pass

    print("#{}".format(test_case))
    # ///////////////////////////////////////////////////////////////////////////////////
