class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        size = len(A) + 1
        count = [0] * size

        for val in A:
            count[val] += 1

            res1 = 0
            res2 = 0

        for idx, val in enumerate(count):
            if val == 2:
                res1 = idx
            if val == 0:
                res2 = idx

        return res1, res2

--------------------------------------------------------------------------------------------------------------------------------

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        d = {}
        res = []
        n = len(A)
        sum1 = (n*(n+1))//2
        total = sum(A)
        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
                
        for key, val in d.items():
            if val == 2:
                res.append(key)
                find = sum1-(total-key)
                res.append(find)
                
        return res