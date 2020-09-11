# import sys
#
# sys.stdin = open("sample_input2.txt", "r")
#
# def travel(n, W):
#     D = [[0] * (1 << (n-1)) for _ in range(n)]
#
#     for i in range(1,n):
#         D[i][0] = W[i][0]
#
#     for k in range(n-2):
#         print(V.difference({0,k}))
#         for A in (V.difference({0,k})):
#             for i in range(1,n):
#                 if i in A: continue
#
#     print(D)
#     return
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # ///////////////////////////////////////////////////////////////////////////////////
#     N = int(input())
#     W = [list(map(int, input().split())) for _ in range(N)]
#     W = [[9999 if c == 0 else c for c in r] for r in W]
#     V = {*list(range(N))}
#     print(W)
#     travel(N,W)
#     print(min(4,*[3,5,6,7]))
#     print("#{}".format(test_case))
#     # ///////////////////////////////////////////////////////////////////////////////////
