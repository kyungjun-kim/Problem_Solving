# 링크 주소 : https://leetcode.com/problems/single-number/

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return cnt.most_common(len(nums))[-1][0]
        