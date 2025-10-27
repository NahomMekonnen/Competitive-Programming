class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        new = [i for i in bank if "1" in i]
        cnt = 0
        for i in range(1,len(new)) :
            cnt += new[i-1].count("1") * new[i].count("1")
        return cnt
