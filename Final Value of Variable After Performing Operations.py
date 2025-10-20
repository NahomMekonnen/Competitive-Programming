class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        perform = 0 
        for i in operations :
            if i[0] == "+" or i[-1] == "+" :
                perform += 1
            else :
                perform -= 1
        return perform 
