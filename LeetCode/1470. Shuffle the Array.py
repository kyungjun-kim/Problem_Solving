#문제 링크 : https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return sum(list(map(lambda a,b : [a,b], nums[:n],nums[n:])),[])