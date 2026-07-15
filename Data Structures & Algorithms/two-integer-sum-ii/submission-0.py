class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        i,j = 0, len(n)-1
        while i < j:
            sum = n[i] + n[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            if sum == target:
                return [i+1, j+1] 
        
        
        