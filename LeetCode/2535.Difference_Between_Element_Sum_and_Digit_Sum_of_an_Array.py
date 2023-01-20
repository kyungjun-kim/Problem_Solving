# 문제링크 : https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(list(map(lambda x: int(x) , tuple(''.join(list(map(lambda x : str(x), nums))))))))