class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()
        n = len(nums)
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        left, right = 1, n-1
        if nums[0] + nums[1] + nums[2] > target:
            res.append(nums[0] + nums[1] + nums[2])
        elif nums[0] + nums[n-2] + nums[n-1] < target:
            res.append(nums[0] + nums[n-2] + nums[n-1])
        else:
            while left < right:
                temp = nums[0] + nums[right] + nums[left]
                res.append(temp)
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return temp
        res.append(self.threeSumClosest(nums[1:], target))
        res.sort(key=lambda x: abs(x - target))
        return res[0]


s = Solution()
text = [-1,2,1,-4]

target = 1
print(s.threeSumClosest(text, target))