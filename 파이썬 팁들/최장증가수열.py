from bisect import bisect_left

def lis(sl):
    N = len(sl)
    C = [10000001] * (N + 1)
    C[0] = 0
    LIS = [1] * N

    c_index = 0
    for i, n in enumerate(sl):
        c_index = bisect_left(C, n)
        C[c_index] = n
        LIS[i] = c_index
        # print("i :", i, ", n :", n, ", c_index :", c_index)
        # print("C :", C)
        # print("LIS :", LIS)
    # print(max(LIS))

lis([4,2,5,8,4,11,15])