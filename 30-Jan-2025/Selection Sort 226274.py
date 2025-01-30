# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n-1) :
            minPos = i
            for j in range(i+1,n):
                if(arr[j] < arr[minPos]):
                    minPos = j
            if(minPos != i):
                arr[minPos], arr[i] = arr[i] , arr[minPos]
                