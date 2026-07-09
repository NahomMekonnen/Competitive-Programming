class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        newArr = []
        for i in range(0, len(arr), 2 * k) :
            newArr.append( arr[i: i + 2 * k])
        for i in range(len(newArr)) :
            first = newArr[i][:k]
            first = first[::-1]
            newArr[i] = first + newArr[i][k:]
        ans = ""
        for arr in newArr :
            ans += "".join(arr)
        return ans
