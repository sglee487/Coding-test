import sys

sys.stdin = open("구현-문자열 재정렬.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    S = input()
    cl = []
    nl = []
    number = ['0','1','2','3','4','5','6','7','8','9']
    for c in S:
        if c in number:
            nl.append(int(c))
        else:
            cl.append(c)

    print(f"{''.join(sorted(cl))}{sum(nl)}")