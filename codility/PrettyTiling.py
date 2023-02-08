import sys

sys.setrecursionlimit(10 ** 9)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

answer = 0


def is_answer(A):
    for i in range(len(A) - 1):
        if A[i][1] != A[i + 1][3]:
            return False
    return True


def dfs(step, now, A):
    global answer
    if now == len(A):
        if is_answer(A):
            answer = min(answer, step)
        return

    # nothing
    dfs(step, now + 1, A)

    original = A[now][:]
    # clock
    A[now] = original[3] + original[:3]
    dfs(step + 1, now + 1, A)

    # clockwise
    A[now] = original[1:4] + original[0]
    dfs(step + 1, now + 1, A)

    # opposite
    A[now] = original[2:] + original[:2]
    dfs(step + 2, now + 1, A)

    A[now] = original


def solution(A):
    global answer
    # Implement your solution here
    # print(A)
    answer = 987654321
    dfs(0, 0, A)
    return answer

