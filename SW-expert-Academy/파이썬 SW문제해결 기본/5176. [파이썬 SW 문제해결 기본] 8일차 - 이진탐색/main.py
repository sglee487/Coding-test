import sys

sys.stdin = open("sample_input.txt", "r")

def insert_element(index, data):
    global tree

    if tree[index] == 0:
        tree[index] = data
    else:
        if data < tree[index]:
            insert_element(index*2,data)
        else:
            insert_element(index * 2 + 1,data)

def inorder(n, last):
    global cnt
    if n <= last:
        inorder(n * 2, last)
        tree[n] = cnt
        cnt += 1
        inorder(n * 2 + 1, last)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    # tree = [0] * ((2**(N.bit_length()))+1)
    tree = [0] * (N+1)
    cnt = 1
    inorder(1, N)
    print('#{} {} {}'.format(test_case+1, tree[1], tree[N // 2]))

    # ///////////////////////////////////////////////////////////////////////////////////
