import sys

sys.stdin = open("sample_input.txt", "r")

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
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    Head = None
    for item in numbers:
        Node.addToLast(Head,item)


    for _ in range(M-1):
        InsertNumbers = list(map(int, input().split()))

        new_node = Node(InsertNumbers[0])
        node = new_node
        for item in InsertNumbers[1:]:
            node.link = Node(item)
            node = node.link

        new_last_node = node

        # 처음에 있을 경우
        if Head.item > InsertNumbers[0]:
            new_last_node.link = Head
            Head = new_node
            continue

        # 중간에 있을 경우
        MT = False
        node = Head
        pre_node = None
        while node != None:
            if node.item > InsertNumbers[0]:
                pre_node.link = new_node
                new_last_node.link = node
                MT = True
                break
            pre_node = node
            node = node.link
        if MT: continue

        # 끝까지 못 찾은 경우 (끝에 붙여야 한다)
        pre_node.link = new_node

    result_list = []
    node = Head
    while node != None:
        result_list.append(node.item)
        node = node.link
    print("#{}".format(test_case),*result_list[:-11:-1])

    # ///////////////////////////////////////////////////////////////////////////////////
