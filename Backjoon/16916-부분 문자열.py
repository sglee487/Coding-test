import sys

sys.setrecursionlimit(10 ** 9)

sys.stdin = open("16916-부분 문자열-6.txt", "r")

input = sys.stdin.readline

A:str = input().strip()
B:str = input().strip()
nextp = [-1] * len(B)

# p: 패턴, M: 패턴의 길이
# nextp: 불일치가 발생하면 이동할 위치를 저장
def KMP_Preprocess(p, nextp):
    M = len(p)
    i = 0; j = -1

    while i<M:
        nextp[i] = j
        while j >= 0 and p[i] != p[j]:
            j = nextp[j]

        i += 1; j += 1

KMP_Preprocess(B, nextp)

# t: 텍스트, p: 패턴
# N: 텍스트의 길이, M: 패턴의 길이
# nextp: 불일치가 발생하면 이동할 위치를 저장
def KMP_Search(t,p,nextp):
    N = len(t); M = len(p)
    i = 0; j = 0

    while i < N:
        while j >= 0 and t[i] != p[j]:
            j = nextp[j]
        i += 1; j += 1
        if j == M:
            return i-j
    return -1

print(1 if KMP_Search(A,B,nextp) != -1 else 0)