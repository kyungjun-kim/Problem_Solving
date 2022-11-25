# 문제 링크 : https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return list(map(lambda x : nums[x] , nums))