import numpy as np

def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


def is_fit(keybox, lockbox):
    for i in range(len(lockbox)):
        for j in range(len(lockbox[0])):
            if keybox[i][j] + lockbox[i][j] != 1:
                return False
    return True


def solution(key, lock):
    keys = []
    keys.append(key)
    keys.append(rotate_a_matrix_by_90_degree(keys[0]))
    keys.append(rotate_a_matrix_by_90_degree(keys[1]))
    keys.append(rotate_a_matrix_by_90_degree(keys[2]))

    upr, downr = len(lock), 0
    leftc, rightc = len(lock[0]), 0
    for r in range(len(lock)):
        for c in range(len(lock[0])):
            if lock[r][c] == 0:
                upr = min(r, upr)
                downr = max(r, downr)
                leftc = min(c, leftc)
                rightc = max(c, rightc)
    if upr == len(lock): return True

    interestlock = np.array(lock)[upr:downr + 1, leftc:rightc + 1]
    for i in range(4):
        for r in range(len(keys[i]) - len(interestlock) + 1):
            for c in range(len(keys[i][0]) - len(interestlock[0]) + 1):
                if is_fit(np.array(keys[i])[r:r + len(interestlock), c:c + len(interestlock[0])], interestlock):
                    return True
    return False