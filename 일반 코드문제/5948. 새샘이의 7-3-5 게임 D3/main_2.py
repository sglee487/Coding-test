"code from : john1752"
import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
result = []
for test_case in range(1,1+T):
    i = list(map(int,input().split()))
    add = []
    for a in range(len(i)):
        for b in range(a+1,len(i)):
            for c in range(b+1,len(i)):
                add.append(i[a]+i[b]+i[c])
    result.append(sorted(set(add))[-5])
for res in range(len(result)):
    print("#{} {}".format(res+1,result[res]))