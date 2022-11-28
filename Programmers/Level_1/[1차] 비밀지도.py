def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2) :
        #print(i,j, bin(i | j))
        num = ""
        for k in bin(i | j)[2:] :
            if k == "1" :
                num += "#"
            elif k == "0" :
                num += " "
        #num = num.replace("  ",' ')
        if len(num) < n :
            num = ' '*(n-len(num)) + num
        answer.append(num)
   # print(answer)
    return answer