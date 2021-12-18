class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        for q1, q2, r in queries:
            
            cur_count = 0
            
            for p1, p2 in points:
                
                dist = (((p1-q1)**2) + ((p2-q2)**2))**(1/2)
                cur_count += (dist <= r)
                
            ans.append(cur_count)
            
        return ans
        
