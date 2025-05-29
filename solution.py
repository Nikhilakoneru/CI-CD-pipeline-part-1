class Solution:
    def majorityElement(self, nums: list[int]) -> int:
      
        candidate = None
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if num == candidate else -1
        return candidate