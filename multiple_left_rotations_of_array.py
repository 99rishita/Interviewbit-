class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        res = []
        n = len(A)
        for b in B:
            res.append(A[b%n:]+A[:b%n])
        return res
