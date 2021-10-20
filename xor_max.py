class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer


    def twoint(a,b):
        return ((a | b) & (~a | ~b))

    def solve(self, A, B):
        max = 0
        for a in A:
            for b in B:
                if(self.twoint(a,b) > max):
                    max = self.twoint(a,b)
        return max

