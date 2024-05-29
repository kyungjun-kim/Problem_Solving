def solution(prices):
    answer = list(range(len(prices)-1,-1,-1))
    stack = []
    for i, j in enumerate(prices) :
        cnt = 1
        while stack != [] and j < stack[-1][1] :
            p = stack.pop()
            answer[p[0]] = i - p[0]
            cnt += 1          
        if stack == [] or stack[-1][1] <= j :
            stack.append([i,j])            
    return answer
    