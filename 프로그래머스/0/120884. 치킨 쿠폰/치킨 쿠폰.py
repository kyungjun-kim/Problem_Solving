def solution(chicken):
    answer = chicken // 10
    cou = chicken // 10 + chicken % 10
    while cou >= 10 :
        tmp = cou // 10
        answer += tmp
        cou %= 10
        cou += tmp
    return answer