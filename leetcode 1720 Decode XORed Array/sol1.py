class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ans = [first]
        
        for enc_num in encoded:
            dec_num = ans[-1] ^ enc_num
            ans.append(dec_num)
            
        return ans
