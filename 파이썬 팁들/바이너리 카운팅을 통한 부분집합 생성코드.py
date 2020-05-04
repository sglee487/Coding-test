# 파이썬 SW문제해결 응용_구현 - 02 완전 검색
# 2차시 02 조합적 문제
arr = [2,3,4,5]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1 << j):
            print(arr[j], end=',')
    print()

arr = [2,3,4,5]
for i in range(1 << len(arr)):
    print([arr[j] for j in range(len(arr)) if i & (1 << j)])