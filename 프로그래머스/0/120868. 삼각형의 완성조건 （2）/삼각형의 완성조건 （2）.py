def solution(sides):
    answer = 0
    sides = sorted(sides)
    for i in range(1,3001) :
        if sides[0] + i > sides[1] and i < sum(sides) and sides[1] + i > sides[0]:
            answer += 1
    return answer