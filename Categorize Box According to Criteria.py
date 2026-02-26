class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length * width * height 
        bulky, heavy = False, False
        if vol >= 10e8 or (length >= 10e3 or width >= 10e3 or height >= 10e3 ) :
            bulky = True
            
        if mass >= 100 :
            heavy = True
        ans = "Neither"
        if heavy and bulky :
            ans = "Both"
        elif heavy :
            ans = "Heavy"
        elif bulky :
            ans = "Bulky" 
        return ans
