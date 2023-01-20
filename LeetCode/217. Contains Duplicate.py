# 문제링크 : https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)) :
            return False
        else :
            return True