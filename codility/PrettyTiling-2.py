# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
sys.setrecursionlimit(10 ** 9)

answer = 987654321

def solution(A):
    # Implement your solution here
    answer = 987654321

    N = len(A)
    for i in range(4):
        rotate = i if i != 3 else 1
        prev_r = (1+i)%4
        prev_c = A[0][prev_r]
        for j in range(1, N):
            match_r = A[j].index(prev_c)
            rotate += abs(3-match_r) if match_r != 0 else 1
            prev_r = (match_r + 2) % 4
            prev_c = A[j][prev_r]
        answer = min(answer, rotate)
    return answer
