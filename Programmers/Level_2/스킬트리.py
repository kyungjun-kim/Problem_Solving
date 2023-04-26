# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/49993
import re
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees :
        if skill.startswith(''.join(re.findall('|'.join(skill), i))) :
            answer += 1
    return answer