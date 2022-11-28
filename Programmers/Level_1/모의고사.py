def solution(answers):
    num = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5],[0,0,0]]
    for i in range(3) :
        for j in range(len(answers)) : 
                if answers[j] == num[i][j%len(num[i])] :
                    num[3][i] += 1
    answer = [i + 1 for i, value in enumerate(num[3]) if value == max(num[3])]
    return answer