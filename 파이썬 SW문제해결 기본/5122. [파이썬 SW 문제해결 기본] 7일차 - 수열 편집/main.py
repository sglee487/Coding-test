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
                print(p.item, end=' ')
                p = p.link
            print()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))

    Head = None
    for item in numbers:
        Node.addToLast(Head,item)

    for _ in range(M):
        command_list = list(input().split())
        if command_list[0] == 'I':
            # Head에 넣는 경우
            if int(command_list[1]) == 0:
                new_node = Node(int(command_list[2]),Head)
                Head = new_node
            else:
                pre_node = None
                node = Head
                for _ in range(int(command_list[1])):
                    pre_node = node
                    node = node.link
                new_node = Node(int(command_list[2]),node)
                pre_node.link = new_node
        if command_list[0] == 'D':
            # Head를 지우는 경우
            if int(command_list[1]) == 0:
                Head = Head.link
            else:
                pre_node = None
                node = Head
                for _ in range(int(command_list[1])):
                    pre_node = node
                    node = node.link
                pre_node.link = node.link
        if command_list[0] == 'C':
            node = Head
            for _ in range(int(command_list[1])):
                node = node.link
            node.item = int(command_list[2])

    result = 0
    node = Head
    for _ in range(L):
        node = node.link
        if node == None:
            break
    if node == None:
        result = -1
    else:
        result = node.item

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
