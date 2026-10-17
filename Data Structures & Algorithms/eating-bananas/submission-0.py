import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        k_lower = 1
        k_upper = max(piles)
        answer = k_upper
        while k_upper >= k_lower:
            mid = (k_lower + k_upper) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours > h:
                k_lower = mid + 1
            elif hours <= h:
                answer = mid
                k_upper = mid - 1
        
        return answer
            

        




        
        