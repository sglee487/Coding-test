import sys

sys.stdin = open("sample_input.txt", "r")

class Node:
    def __init__(self,item,leftlink=None,rightlink=None):
        self.item = item
        self.leftlink = leftlink
        self.rightlink = rightlink

def preorder_traverse(T):
    if T:
        # visit(T)
        preorder_traverse(T.leftlink)
        preorder_traverse(T.rightlink)

def inorder_traverse(T):
    if T:
        preorder_traverse(T.leftlink)
        # visit(T)
        preorder_traverse(T.rightlink)

def inorder_traverse(T):
    if T:
        preorder_traverse(T.leftlink)
        preorder_traverse(T.rightlink)
        # visit(T)

def preorder_traverse_for_result(T):
    global result
    if T:
        # visit(T)
        preorder_traverse_for_result(T.leftlink)
        preorder_traverse_for_result(T.rightlink)
        result += 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    E, N = map(int, input().split())
    nodelist = [0] * (E+2)
    for i in range(E+1):
        nodelist[i+1] = Node(i+1)

    input_list = list(map(int, input().split()))
    for p,c in zip(input_list[0::2],input_list[1::2]):
        if nodelist[p].leftlink == None:
            nodelist[p].leftlink = nodelist[c]
        else:
            nodelist[p].rightlink = nodelist[c]

    result = 0
    preorder_traverse_for_result(nodelist[N])

    print("#{}".format(test_case),result)

    # ///////////////////////////////////////////////////////////////////////////////////
