import sys

sys.stdin = open("sample_input2.txt", "r")

class Node:
    def __init__(self, item, link=None):
        self.item = item
        self.link = link

    def addToFirst(self,data):
        global Head
        Head = Node(data,Head)

    def add(self,pre, data):
        if pre == None:
            print('error')
        else:
            pre.link = Node(data, pre.link)

    def addToLast(self,data):
        global Head
        if Head == None:
            Head = Node(data, None)
        else:
            p = Head
            while p.link != None:
                p = p.link
            p.link = Node(data, None)

    def printall(self):
        if self == None:
            print("empty")
        else:
            p = self
            while p != None:
                print(p.item)
                p = p.link

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    Head = None
    for item in numbers:
        Node.addToLast(Head,item)
    last_node = Head
    while last_node.link != None:
        last_node = last_node.link
    last_node.link = Head

    pre_node = Head
    node = Head.link
    for _ in range(K):
        for _ in range(M-1):
            pre_node = node
            node = node.link

        # 리스트의 맨 끝일 경우 head만 더해야 함.
        if node == Head:
            new_node = Node(pre_node.item + node.item, node)
            pre_node.link = new_node
            pre_node = new_node
        else:
            new_node = Node(pre_node.item + node.item, node)
            pre_node.link = new_node
            pre_node = new_node


    result_list = []
    node = Head
    while True:
        result_list.append(node.item)
        node = node.link
        if node == Head: break
    print("#{}".format(test_case),*result_list[:-11:-1])

    # ///////////////////////////////////////////////////////////////////////////////////
