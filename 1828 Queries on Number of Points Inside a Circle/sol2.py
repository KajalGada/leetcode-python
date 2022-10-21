class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        count = []
        
        for each_q in queries:
            cx, cy, r = each_q
            cur_count = 0
            
            for each_p in points:
                dist = math.dist(each_p, [cx,cy])
                cur_count += (dist <= r)
                    
            count.append(cur_count)
        
        
        return count
        
