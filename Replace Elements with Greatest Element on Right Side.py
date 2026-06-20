class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        el, maxEl = -1, -1
        for i in range(len(arr) - 1, -1, -1) :
            maxEl = max(maxEl, el)
            el = arr[i]
            arr[i] = maxEl
        return arr
