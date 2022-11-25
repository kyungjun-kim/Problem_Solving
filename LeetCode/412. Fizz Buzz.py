# 링크 주소 : https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) :
        return list(map(lambda x: 'FizzBuzz' if x % 15 == 0 
         else 'Fizz' if x % 3 == 0 
         else 'Buzz' if x % 5 == 0 
         else str(x)
         , range(1,n+1) ))
        