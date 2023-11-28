class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        def threeSum(start, target):
            three = []
            
            def twoSum(start, target):
                two = []
                left = start
                right = length - 1

                while left < right:
                    sum = nums[left] + nums[right]

                    if sum == target:

                        two.append([nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif sum < target:
                        left += 1

                    else:
                        right -= 1

                return two
            
            i = start
            while i < length - 2:
                if nums[i] == nums[i - 1] and i > start:
                    i += 1
                    continue

                for tw in twoSum(i + 1, target - nums[i]):
                    three.append([nums[i]] + tw)

                i += 1
            
            return three
            

        nums = sorted(nums)
        result = []

        i = 0
        while i < length - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            for th in threeSum(i + 1, target - nums[i]):
                result.append([nums[i]] + th)
            i += 1

        return result