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
    N = int(input())

    input_element = list(map(int, input().split()))

    minheap = MinHeap()
    for element in input_element:
        minheap.insert(element)
    result = 0
    result_index = N//2
    while result_index > 0:
        result += minheap.tree_list[result_index]
        result_index = result_index // 2

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
