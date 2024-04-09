def solution(age):
    answer = ''
    a = list(map(lambda x : chr(x), range(97,107)))
    for i in str(age) :
        answer += a[int(i)]
    return answer