# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = [set(word) for word in words]
        maxProd = 0
        for i in range (len(sets)) :
            for j in range(i+1,len(sets)) :
                if len(sets[i]&sets[j]) == 0 :
                    maxProd = max(maxProd, (len(words[i]*len(words[j]))))
        return maxProd