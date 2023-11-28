class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #kadane's algorithm
        sum = 0
        maximum = float('-inf')

        for i in nums:
            sum = max(i, sum + i)
            maximum = max(maximum, sum)

        return maximum