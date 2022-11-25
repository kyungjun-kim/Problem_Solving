#문제 링크 : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while (num >= 1) :
            answer += 1
            if num == 1 :
                break
            if num % 2 == 0 :
                num /= 2 
            else :
                num -= 1
        return answer