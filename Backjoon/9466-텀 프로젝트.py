from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("9466-텀 프로젝트-1.txt", "r")

input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    N = int(input())
    sl = list(map(int, input().split()))
    sl.insert(0,0)
    teams = 0
    # 0은 아직 계산 안함, 1은 계산중, 2은 팀 없음, 3은 팀 있음
    calculed = [0] * (N+1)
    for start in range(1, N+1):
        if calculed[start]: continue
        journey = []
        idict = defaultdict(int)
        s = start
        while not calculed[s]:
            calculed[s] = 1
            idict[s] = len(journey)
            journey.append(s)
            s = sl[s]
        if calculed[s] == 1:
            for ns in journey[:idict[s]]:
                calculed[ns] = 2
            for ns in journey[idict[s]:]:
                calculed[ns] = 3
        elif calculed[s] >= 2:
            for ns in journey:
                calculed[ns] = 2

    print(calculed.count(2))