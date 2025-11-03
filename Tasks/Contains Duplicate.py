class Solution(object):
    def containsDuplicate(self, nums):
        if list(set(nums)) != nums and len(nums) != len(set(nums)):
            return True
        return False
