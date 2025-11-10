class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for x in nums[1:]:
            result ^= x
        return result

sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))