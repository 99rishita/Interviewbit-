class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        res = []
        res.append([1])
        res.append([1,1])
        if A == 0:
            return res[0]
        if A == 1:
            return res[1]
        for i in range(2, A+1):
            j = 1
            d = [1,1]
            k = res[-1]
            while j < i:
                d.insert(j, k[j-1]+k[j])
                j += 1
            res.append(d)
            
        return res[A]
