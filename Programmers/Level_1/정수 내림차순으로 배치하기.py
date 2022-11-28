def solution(n):
    n_list = []
    answer = ''
    for i in range(len(str(n))):
        n_list.append(str(n)[i])
    n_list.sort(reverse = True)
    for i in n_list :
        answer += i
    return int(answer)