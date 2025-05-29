class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        if not nums:
            raise ValueError("nums is non empty list")

        ft = type(nums[0])
        for x in nums:
            if not isinstance(x, ft):
                raise TypeError("All elements must be of the same type")
                
        candidate = None
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            vote += 1 if num == candidate else -1
        return candidate
