import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("2666-벽장문의 이동-2.txt", "r")

input = sys.stdin.readline

def dfs(closet, a, b, move, step):
    global L, answer, sequence
    if step == L:
        # print(move)
        answer = min(answer, move)
        return
    target = sequence[step]
    ma = abs(target - a)
    closet[a] = 1
    closet[target] = 0
    dfs(closet, target, b, move+ma, step+1)
    closet[a] = 0
    closet[target] = 1

    mb = abs(target - b)
    closet[b] = 1
    closet[target] = 0
    dfs(closet, a, target, move+mb, step+1)
    closet[b] = 0
    closet[target] = 1
    return

N = int(input())
closets = [1] * (N+1)
a, b = map(int, input().split())
closets[a] = 0
closets[b] = 0
L = int(input())
sequence = []
for _ in range(L):
    sequence.append(int(input()))
# print(closets)
# print(sequence)
answer = 987654321
dfs(closets[:], a, b, 0, 0)
print(answer)