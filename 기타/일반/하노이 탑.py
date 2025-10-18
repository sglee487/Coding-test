import sys

sys.setrecursionlimit(10 ** 9)

# input = sys.stdin.readline

N = 1

def hanoi_move(n, src, mid, dst):
    if n <= 0:
        return []
    # 그런 건 난 모르겠고, 모두 가운데로 옮겨
    left = hanoi_move(n-1, src, dst, mid)
    # 내가 하고 싶은거
    move = [(src, dst)]
    # 그런 건 난 모르겠고, 다시 가운데에서 오른쪽으로 옮겨
    right = hanoi_move(n-1, mid, src, dst)
    return left + move + right

def hanoi_print(n):
    moves = hanoi_move(n, 'A', 'B', 'C')
    print(*moves, sep='\n')

hanoi_print(N)