import sys

sys.stdin = open("sample_input.txt", "r")
# https://wayhome25.github.io/cs/2017/04/19/cs-23/
class MinHeap:
    def __init__(self):
        self.tree_list = [None, ]
        self.num_of_data = 0 # 마지막 데이터의 index

    def is_go_up(self, idx, data):
        if idx <= 1:
            return False

        parent_value = self.tree_list[idx // 2]

        if parent_value < data:
            return False
        else:
            return True

    def insert(self, data):
        if self.num_of_data == 0:
            self.tree_list.append(data)
            self.num_of_data += 1
            return

        self.tree_list.append(data)
        self.num_of_data += 1

        idx_data = self.num_of_data

        while self.is_go_up(idx_data, data):
            parent_idx = idx_data // 2
            self.tree_list[idx_data] = self.tree_list[parent_idx]
            idx_data = parent_idx

        self.tree_list[idx_data] = data


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, L = map(int, input().split())

    tree = [0] * (N + 2)
    for _ in range(M):
        index, data = map(int,input().split())
        tree[index] = data

    index = N + (N % 2 == 0)
    while index > 0:
        tree[index//2] = tree[index] + tree[index-1]
        index -= 2

    print("#{}".format(test_case),tree[L])

    # ///////////////////////////////////////////////////////////////////////////////////
