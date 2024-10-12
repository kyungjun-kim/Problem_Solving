array = []
s = ''
max_len = 0
for i in range(5) :
    tmp = input()
    if len(tmp) > max_len :
        max_len = len(tmp)
    array.append(list(map(lambda x : x, tuple(tmp))))
tmp = 0
for i in range(max_len) :
    for j in array :
        if len(j) > tmp :
            s += j[tmp]
    tmp += 1
print(s)