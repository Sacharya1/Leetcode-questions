class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        primeList = [1]*(n+1)
        p = 2
        result = list()

        while (p*p <= n):
            if primeList[p]:
                for i in range(p*p, n+1, p):
                    primeList[i] = 0
            p += 1

        for i in range(2, (n//2+1)):
            if primeList[i] and primeList[n-i]:
                result.append([i, n-i])
                
        return result
