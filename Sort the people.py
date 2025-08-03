# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = dict(zip(heights,names))
        heights = sorted(heights,reverse = True)
        ans = []
        for i in heights:
            ans.append(people[i])
        return ans
