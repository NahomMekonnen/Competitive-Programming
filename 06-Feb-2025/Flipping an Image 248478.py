# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            l , r = 0 , (len(image[i]) -1)
            while (l < r):
                image[i][l] , image[i][r] = image[i][r], image[i][l]
                l += 1
                r -= 1
            for j in range(len(image[i])):
                image[i][j] = 0 if image[i][j] == 1 else 1
        
        return image


