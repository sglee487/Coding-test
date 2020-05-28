# import sys
# from collections import deque
#
# sys.stdin = open("sample_input.txt", "r")
#
# def Dijkstra(G, r, result):
#     D = [INF] * (N+1)
#     P = [None] * (N+1)
#     visited = [False] * (N+1)
#     D[r] = 0
#     P[1] = 1
#
#     for _ in range(N):
#         minIndex = -1
#         min = INF
#         for i in range(N):
#             if not visited[i] and D[i] < min:
#                 min = D[i]
#                 minIndex = i
#         visited[minIndex] = True
#         result += D[minIndex]
#         if P[minIndex] != 1:
#             result -= D[P[minIndex]]
#         while G[minIndex]:
#             v, val = G[minIndex].pop()
#             if not visited[v] and D[minIndex] + val < D[v]:
#                 D[v] = D[minIndex] + val
#                 P[v] = minIndex
#     return D,P, result
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # ///////////////////////////////////////////////////////////////////////////////////
#     N, M = map(int, input().split())
#     INF = float('INF')
#
#     G = [deque() for _ in range(N+1)]
#     for i in range(M):
#         v1, v2, d = map(int, input().split())
#         G[v1].append((v2,d))
#         G[v2].append((v1, d))
#
#     # print(G)
#     result = 0
#     D, P,result = Dijkstra(G, 1,result)
#     # print(D)
#     # print(P)
#
#     # for i in range(2,N+1):
#     #     result += D[i]
#     #     if P[i] != 1:
#     #         result -= D[P[i]]
#     print("#{}".format(test_case),result)
#     # ///////////////////////////////////////////////////////////////////////////////////
