class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        res = 0
        rev_lsb = 0
        for i in range(32):
            lsb = A & 1
            rev_lsb = lsb << (31-i)
            res = res|rev_lsb
            A = A >> 1
        return res