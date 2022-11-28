def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr2)) :
        for j in range(len(arr2[0])) :
            answer[i][j] += arr2[i][j]
    return answer