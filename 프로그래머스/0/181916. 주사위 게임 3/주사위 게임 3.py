def solution(a, b, c, d):
    result = sorted([a,b,c,d], key = lambda k : [[a,b,c,d].count(k), k])
    if len(set(result)) == 1:
        return 1111 * a
    elif len(set(result)) == 4:
        return min(result)
    elif len(set(result)) == 3:
        return result[0] * result[1]
    elif len(set(result)) == 2 and result[1] != result[2]:
        return (result[0] + result[-1]) * abs(result[0] - result[-1])
    else :
        return (10 * result[-1] + result[0]) ** 2