import numpy as np

# https://github.com/ndb796/Python-Competitive-Programming-Team-Notes/blob/master/Miscellaneous/rotate_a_matrix_by_90_degree.py
def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

def isfit(matrix):
    # print(matrix)
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] != 1: return False
    return True

def solution(key, lock):
    if isfit(lock): return True
    N = len(lock)
    M = len(key)
    keys = []
    keys.append(key)
    keys.append(rotate_a_matrix_by_90_degree(keys[0]))
    keys.append(rotate_a_matrix_by_90_degree(keys[1]))
    keys.append(rotate_a_matrix_by_90_degree(keys[2]))

    lock_with_padding = np.array([[0] * (N+(M-1)*2) for _ in range((N+(M-1)*2))])
    lock_with_padding[(M-1):(M-1+N),(M-1):(M-1+N)] = lock[:]
    # print(*lock_with_padding,sep='\n')
    NM = len(lock_with_padding)
    # print(NM)
    for r in range(NM-(M-1)):
        for c in range(NM-(M-1)):
            for key in keys:
                lock_with_padding[r:r+M,c:c+M] += key
                # print(r,c)
                # print(lock_with_padding)
                if isfit(lock_with_padding[(M-1):(M-1+N),(M-1):(M-1+N)]): return True
                lock_with_padding[r:r + M, c:c + M] -= key

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]),True)