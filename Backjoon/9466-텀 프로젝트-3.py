from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("9466-텀 프로젝트-1.txt", "r")

input = sys.stdin.readline

def circulate(now):
    global answer
    if completed[now]: return
    nxt = nl[now]
    if now in processing and not completed[now]:
        answer -= 1
        completed[now] = True
        circulate(nxt)
        return
    processing.add(now)
    circulate(nxt)
    completed[now] = True


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    nl = list(map(int, input().split()))
    answer = n
    nl.insert(0,0)
    N = len(nl)
    completed = [False] * N
    for i in range(1, N):
        processing = set()
        circulate(i)
    print(answer)