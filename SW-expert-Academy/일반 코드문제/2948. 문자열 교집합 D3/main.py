import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # https://dongyeopgu.github.io/algorithm/d3/swea-d3.html
    N, M = map(int, input().split())

    set_1 = set(input().split())
    set_2 = set(input().split())
    result = set_1 & set_2

    # n_words = list(input().split())
    # m_words = list(input().split())
    #
    # n_words.sort()
    # m_words.sort()
    #
    # n_index = 0
    # m_index = 0
    #
    # count = 0
    # while n_index < N and m_index < M:
    #     if n_words[n_index] == m_words[m_index]:
    #         count += 1
    #         n_index += 1
    #         m_index += 1
    #     elif n_words[n_index] > m_words[m_index]:
    #         m_index += 1
    #     elif n_words[n_index] < m_words[m_index]:
    #         n_index += 1

    print("#{}".format(test_case), len(result))
    # ///////////////////////////////////////////////////////////////////////////////////
