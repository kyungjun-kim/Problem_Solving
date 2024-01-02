# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133499#

def solution(babbling):
    answer = 0
    for i in babbling :
        if 'aya'*2 in i or 'ye'*2 in i or 'woo'*2 in i or 'ma'*2 in i:
            continue
        elif i.replace("aya",' ').replace("ye",' ').replace("woo",' ').replace("ma",' ').replace(" ",'') == '' :
            answer += 1
    return answer