#문제 링크 : https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(map(lambda x,y : sum(nums[:y+1]), nums,range(len(nums))))