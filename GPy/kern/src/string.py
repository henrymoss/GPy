import numpy as np
from .kern import Kern


class StringKernel(Kern):
    """
    String Kernel
    """
    def __init__(self, name='sk'):
        super(StringKernel, self).__init__(1, 1, name)

    def calc_k(self, s1, s2):
        """
        Do the actual kernel calculation
        """
        n = len(s1)
        m = len(s2)
        dp = [[1.0] * (m + 1)] * (n + 1)
        p = [0.0] * (m + 1)
        for i in xrange(1, n + 1):
            last = 0
            p[0] = 0
            for k in xrange(1, m + 1):
                p[k] = p[last]
                if s2[k - 1] == s1[i - 1]:
                    p[k] = p[last] + dp[i - 1][k - 1]
                    last = k
            for k in xrange(1, m + 1):
                dp[i][k] = dp[i - 1][k] + p[k]
        return dp[n][m]
        
