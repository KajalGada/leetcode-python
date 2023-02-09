class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        if len(nums) < 3:
            return False

        nums_count = {}

        # Count the numbers
        for n in nums:
            if n in nums_count:
                nums_count[n] += 1
            else:
                nums_count[n] = 1

        can_take = {}
        next_num = 0
        ans = True

        for n in nums:
            if nums_count[n]:
                nums_count[n] -= 1

                # Can it join an existing sequence?
                if (n in can_take) and can_take[n]:
                    can_take[n] -= 1
                    next_num = n + 1

                # Can it make its own sequence (min 3)
                elif ((n+1) in nums_count and nums_count[n+1]) and ((n+2) in nums_count and nums_count[n+2]):
                    nums_count[n+1] -= 1
                    nums_count[n+2] -= 1
                    next_num = n + 3

                # Can't split array into subsequence
                else:
                    ans = False
                    break

                # Mark the next num it can take in the seq
                if next_num in can_take:
                    can_take[next_num] += 1
                else:
                    can_take[next_num] = 1

        return ans
