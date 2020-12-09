import sys

sys.stdin = open("이진탐색-공유기 설치.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, C = map(int, input().split())
    hl = []
    for _ in range(N):
        hl.append(int(input()))
    hl.sort()
    # print(hl)
    ld, rd = 1, hl[-1]-hl[0]
    while ld!=rd:
        mid = (ld+rd) // 2
        s = 1
        now = hl[0]
        for e in hl[1:]:
            if now+mid < e:
                s += 1
                now = e
        if s >= C:
            ld = mid+1
        else:
            rd = mid-1
        # print(ld,rd)
    print(ld)