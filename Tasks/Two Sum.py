class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i
    
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in num_map and num_map[comp] != i:
                return [i, num_map[comp]]
