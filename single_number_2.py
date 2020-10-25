class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for i in range(len(A)):
            ones = (ones^A[i])&(~twos)
            twos = (twos^A[i])&(~ones)
        return ones