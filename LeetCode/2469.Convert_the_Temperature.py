# 문제 링크 : https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer = [celsius + 273.15 , celsius * 1.80 + 32.00]
        return answer