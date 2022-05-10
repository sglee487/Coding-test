import sys
sys.setrecursionlimit(10**9)

sys.stdin = open("NUMBERGAME-1.txt", "r")

input = sys.stdin.readline


def play(left, right):
    global cache, nl
    if cache[left][right] != -1001:
        return cache[left][right]

    if left > right:
        cache[left][right] = 0
        return cache[left][right]

    leftResult = nl[left] - play(left+1, right)
    rightResult = nl[right] - play(left, right-1)
    choiceOne = max(leftResult, rightResult)
    if right - left >= 2:
        leftSkipResult = -play(left+2, right)
        rightSkipResult = -play(left, right-2)
        choiceTwo = max(leftSkipResult, rightSkipResult)
        cache[left][right] = max(choiceOne, choiceTwo)
        return cache[left][right]
    cache[left][right] = choiceOne
    return choiceOne


C = int(input())
for _ in range(C):
    n = int(input())
    nl = list(map(int, input().split()))
    cache = [[-1001] * (n+1) for _ in range(n+1)]
    print(play(0, n-1))