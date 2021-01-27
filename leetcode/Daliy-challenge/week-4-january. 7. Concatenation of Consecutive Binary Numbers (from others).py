class Solution:
    MOD = 10 ** 9 + 7
    A = [0]
    for num in range(1, 10**5 + 1):
        A.append(((A[-1] << num.bit_length()) + num) % MOD)

    def concatenatedBinary(self, n: int) -> int:
        return Solution.A[n]



print(Solution.concatenatedBinary(None,1),1)
print(Solution.concatenatedBinary(None,3),27)
print(Solution.concatenatedBinary(None,12),505379714)