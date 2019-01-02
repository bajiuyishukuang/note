class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res, n = [], len(nums)
        for index, num in enumerate(nums[:-2]):
            left, right = index + 1, n - 1
            min_ = num + nums[left] + nums[left + 1]
            if min_ > target:
                res.append(min_)
                break
            elif num + nums[right] + nums[right - 1] < target:
                res.append(num + nums[right] + nums[right - 1])
            else:
                while left < right:
                    temp = num + nums[left] + nums[right]
                    res.append(temp)
                    if temp > target:
                        right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        return target
        res.sort(key=lambda x: abs(x - target))
        return res[0]

s = Solution()

nums = [-1 , 1, ]