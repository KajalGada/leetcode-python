class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)
        maxCandiesBool = []
        
        for numCandies in candies:
            maxCandiesBool.append(numCandies + extraCandies >= maxCandies)
            
        return maxCandiesBool
        
