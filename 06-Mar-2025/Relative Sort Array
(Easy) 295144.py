# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s, check = len(arr1), defaultdict(int)

        for i in range(len(arr2)) :
            check[arr2[i]] = i + 1

        left, count = [], defaultdict(int)

        for i in arr1 :
            if check[i] == 0 :
                s -= 1
                left.append(i)
            else :
                count[i] += 1

        arr = [0] * s
        check[arr2[0]] = 0
        for i in range(1,len(arr2)) :
            check[arr2[i]] = check[arr2[i-1]] + count[arr2[i-1]]
        
        for i in check :
            while count[i] > 0 :
                arr[check[i]] = i
                count[i] -= 1
                check[i] += 1
                

        left.sort()

        return arr + left
