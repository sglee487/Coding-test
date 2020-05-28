# import sys
# from collections import deque
#
# sys.stdin = open("sample_input.txt", "r")
#
# def checkS(S):
#     pdq = deque()
#     pq = 0
#     i,j = 0,0
#     ntp = False
#     for index,s in enumerate(S):
#         if s == '(':
#             pq += 1
#         elif s == ')': pq -= 1
#         elif s == 'e': return
#         if pq == -1:
#             ntp = True
#             i = index
#
#
# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     # ///////////////////////////////////////////////////////////////////////////////////
#     L = int(input())
#     S = input()
#     S += 'e'
#     i,j = 0,0
#     print(S)
#
#
#     print("#{}".format(test_case))
#     # ///////////////////////////////////////////////////////////////////////////////////
