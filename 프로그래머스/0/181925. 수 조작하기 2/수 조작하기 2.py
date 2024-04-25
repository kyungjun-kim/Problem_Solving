def solution(numLog):
    dic = dict(zip([1,-1,10,-10],["w","s","d","a"]))
    return ''.join(list(map(lambda x,y : dic[x-numLog[y]] , numLog[1:], range(len(numLog)-1))))