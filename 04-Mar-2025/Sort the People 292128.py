# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = [[heights[i], names[i]] for i in range(len(heights))]
        people.sort(reverse=True)
        return [i[1] for i in people]
